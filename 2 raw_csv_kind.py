"""
kind_raw.csv
- request: ccbaKdcd(*지정종목)
- response: ccbaCpno(연계번호)
"""

from utils_raw import *

ccbaKdcd_list = [
    "11", "12", "13", "14", "15", "16", "17", "18",
    "21", "22", "23", "24", "25", "31", "79", "80"
]
find_list = ["ccbaCpno"]
add_list = ["ccbaKdcd"]
kind_df = pd.DataFrame()

for Kdcd in ccbaKdcd_list:
    tmp_df = crawling_process(s_url, find_list, add_list, ccbaKdcd=Kdcd)
    kind_df = pd.concat([kind_df, tmp_df], ignore_index=True)

save_df(kind_df, "kind_raw.csv")
"""
RangeIndex: 15002 entries, 0 to 15001
Data columns (total 2 columns):d
 #   Column         Non-Null Count  Dtype 
---  ------         --------------  ----- 
 0   ccbaCpno_item  15002 non-null  object
 1   ccbaKdcd_item  15002 non-null  object
"""