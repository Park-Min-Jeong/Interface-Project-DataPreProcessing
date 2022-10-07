"""
region_raw.csv
- request: ccbaCtcd(시도코드), ccbaLcto(시군구코드)
- response: ccbaCpno(연계번호)
"""

from utils.crawling import *

ccbaCtcd_list = [
    "11", "21", "22", "23", "24", "25", "26",  # "45",
    "31", "32", "33", "34", "35", "36", "37", "38",
    "50"
]

find_list = ["ccbaCpno"]
add_list = ["ccbaCtcd", "ccbaLcto"]
region_df = pd.DataFrame()

for Ctcd in ccbaCtcd_list:
    Lcto_df = csv_to_df(f"ccbaLcto_{Ctcd}.csv", ccbaLcto_path)
    for Lcto in Lcto_df.iloc[:, 0]:
        if Lcto == 0 or Lcto == "00":
            continue
            # 전체는 삭제
        tmp_df = crawling_process(s_url, find_list, add_list, ccbaCtcd=Ctcd, ccbaLcto=Lcto)
        region_df = pd.concat([region_df, tmp_df], ignore_index=True)

add_list = ["ccbaCtcd"]
for tag in ["45", "ZZ"]:
    tmp_df = crawling_process(s_url, find_list, add_list, ccbaCtcd=tag)
    region_df = pd.concat([region_df, tmp_df], ignore_index=True)

save_df(region_df, "region_raw.csv")
"""
RangeIndex: 14983 entries, 0 to 14982
Data columns (total 3 columns):
 #   Column         Non-Null Count  Dtype 
---  ------         --------------  ----- 
 0   ccbaCpno_item  14983 non-null  object
 1   ccbaCtcd_item  14983 non-null  object
 2   ccbaLcto_item  14832 non-null  object
"""