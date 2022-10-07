"""
location_raw.csv
- request: X
- response: ccbaCpno(연계번호), longitude(경도), latitude(위도)
"""

from utils.crawling import *

find_list = ["ccbaCpno", "longitude", "latitude"]
add_list = []
location_df = pd.DataFrame()

tmp_df = crawling_process(s_url, find_list, add_list)
location_df = pd.concat([location_df, tmp_df], ignore_index=True)

save_df(location_df, "location_raw.csv")
"""
RangeIndex: 15002 entries, 0 to 15001
Data columns (total 3 columns):
 #   Column          Non-Null Count  Dtype 
---  ------          --------------  ----- 
 0   ccbaCpno_item   15002 non-null  object
 1   longitude_item  15002 non-null  object
 2   latitude_item   15002 non-null  object
"""
