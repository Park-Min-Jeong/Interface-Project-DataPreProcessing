"""
name_raw.csv
- request: X
- response: ccbaCpno(연계번호), ccbaMnm1(국문 문화재명)
"""

from utils.crawling import *

find_list = ["ccbaCpno", "ccbaMnm1"]
add_list = []
name_df = pd.DataFrame()

tmp_df = crawling_process(s_url, find_list, add_list)
name_df = pd.concat([name_df, tmp_df], ignore_index=True)

save_df(name_df, "name_raw.csv")
"""
RangeIndex: 15002 entries, 0 to 15001
Data columns (total 2 columns):
 #   Column         Non-Null Count  Dtype 
---  ------         --------------  ----- 
 0   ccbaCpno_item  15002 non-null  object
 1   ccbaMnm1_item  15002 non-null  object
"""