"""
period_raw.csv
- request: ccbaPcd1(*시대)
- response: ccbaCpno(연계번호)
"""

from utils.crawling import *

ccbaPcd1_list = [
    "00", "01", "03", "05", "07", "09",
    "10", "11", "12", "13", "14", "15",
    "20", "30", "40", "45", "50", "60", "99"
]

find_list = ["ccbaCpno"]
add_list = ["ccbaPcd1"]
period_df = pd.DataFrame()

for Pcd1 in ccbaPcd1_list:
    tmp_df = crawling_process(s_url, find_list, add_list, ccbaPcd1=Pcd1)
    period_df = pd.concat([period_df, tmp_df], ignore_index=True)

save_df(period_df, "period_raw.csv")
"""
RangeIndex: 8922 entries, 0 to 8921
Data columns (total 2 columns):
 #   Column         Non-Null Count  Dtype 
---  ------         --------------  ----- 
 0   ccbaCpno_item  8922 non-null   object
 1   ccbaPcd1_item  8922 non-null   object
"""