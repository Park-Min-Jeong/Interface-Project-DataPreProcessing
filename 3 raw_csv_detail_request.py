"""
detail_request.csv
- request: X
- 상세정보 호출용: ccbaAsno(지정번호), ccbaKdcd(종목코드), ccbaCtcd(시도코드)
"""

from utils.crawling import *

find_list = ["ccbaAsno", "ccbaKdcd", "ccbaCtcd"]
add_list = []
detail_request_df = pd.DataFrame()

tmp_df = crawling_process(s_url, find_list, add_list)
detail_request_df = pd.concat([detail_request_df, tmp_df], ignore_index=True)

save_df(detail_request_df, "detail_request_raw.csv")
"""
RangeIndex: 15002 entries, 0 to 15001
Data columns (total 3 columns):
 #   Column         Non-Null Count  Dtype 
---  ------         --------------  ----- 
 0   ccbaAsno_item  15002 non-null  object
 1   ccbaKdcd_item  15002 non-null  object
 2   ccbaCtcd_item  15002 non-null  object
"""
