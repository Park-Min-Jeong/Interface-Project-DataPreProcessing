"""
re_raw.csv
- request:  ccbaPcd1(시대)
- response: ccbaCpno(연계번호),
            ccbaKdcd(종목코드), ccmaName(종목), crltsnoNm(종목번호),
            ccbaMnm1(국문명), ccbaMnm2(한문명),
            ccbaCtcd(시도코드), ccbaCtcdNm(시도명), ccsiName(시군구명),
            ccbaAdmin(관리자), ccbaAsno(관리번호),
            longitude(경도), latitude(위도)
"""
from utils.re_utils import *

ccbaPcd1_list = [
    "00", "01", "03", "05", "07", "09",
    "10", "11", "12", "13", "14", "15",
    "20", "30", "40", "45", "50", "60", "99"
]

find_list = ["ccbaCpno", "ccbaKdcd", "ccmaName", "crltsnoNm",
             "ccbaMnm1", "ccbaMnm2", "ccbaCtcd", "ccbaCtcdNm", "ccsiName",
             "ccbaAdmin", "ccbaAsno", "longitude", "latitude"]

raw_df = pd.DataFrame()

for Pcd1 in ccbaPcd1_list:
    tmp_df = crawling_process(API, find_list, ccbaPcd1=Pcd1)
    raw_df = pd.concat([raw_df, tmp_df], ignore_index=True)

save_df(raw_df, "re_raw.csv")
"""
RangeIndex: 8940 entries, 0 to 8939
Data columns (total 14 columns):
 #   Column           Non-Null Count  Dtype 
---  ------           --------------  ----- 
 0   ccbaCpno_item    8940 non-null   object
 1   ccbaKdcd_item    8940 non-null   object
 2   ccmaName_item    8940 non-null   object
 3   crltsnoNm_item   8940 non-null   object
 4   ccbaMnm1_item    8940 non-null   object
 5   ccbaMnm2_item    8940 non-null   object
 6   ccbaCtcd_item    8940 non-null   object
 7   ccbaCtcdNm_item  8940 non-null   object
 8   ccsiName_item    8940 non-null   object
 9   ccbaAdmin_item   8940 non-null   object
 10  ccbaAsno_item    8940 non-null   object
 11  longitude_item   8940 non-null   object
 12  latitude_item    8940 non-null   object
 13  ccbaPcd1_item    8940 non-null   object
 """