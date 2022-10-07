"""
info_raw.csv
- request: ccbaAsno(지정번호), ccbaKdcd(종목코드), ccbaCtcd(시도코드)
- response: ccbaCpno(연계번호),
            ccmaName(문화재종목), crltsnoNm(지정호수), ccbaMnm1(국문 문화재명), ccbaMnm2(한문 문화재명),
            imageUrl(이미지), content(내용), ccceName(상세시대), ccbaLcad(소재지 상세),
            ccbaAdmin(관리자), ccbaPoss(소유자), ccbaAsdt(지정/등록일)
결과창에서 url 뒤에 ERROR가 나오면 csv_info_2.py 실행
"""

from utils.crawling import *

find_list = ["ccmaName", "crltsnoNm", "ccbaMnm1", "ccbaMnm2",
             "imageUrl", "content",  "ccceName", "ccbaLcad",
             "ccbaAdmin", "ccbaPoss",  "ccbaAsdt"]
# "ccbaCpno" 태그는 item 태그 밖에 있어서 find_list에 넣지 않음
add_list = []
detail_request_df = csv_to_df("detail_request_raw.csv", "./data/raw/")

info_df = pd.DataFrame()
for i in range(len(detail_request_df)):
    target = detail_request_df.iloc[i, :]

    Asno, Kdcd, Ctcd = target[0], target[1], target[2]

    tmp_df = crawling_process(sd_url, find_list, add_list, ccbaAsno=Asno, ccbaKdcd=Kdcd, ccbaCtcd=Ctcd)
    info_df = pd.concat([info_df, tmp_df], ignore_index=True)

save_df(info_df, "info_raw.csv")

"""
RangeIndex: 15002 entries, 0 to 15001
Data columns (total 12 columns):
 #   Column          Non-Null Count  Dtype 
---  ------          --------------  ----- 
 0   ccmaName_item   15002 non-null  object
 1   crltsnoNm_item  15002 non-null  object
 2   ccbaMnm1_item   15002 non-null  object
 3   ccbaMnm2_item   15002 non-null  object
 4   imageUrl_item   14700 non-null  object
 5   content_item    15002 non-null  object
 6   ccceName_item   15002 non-null  object
 7   ccbaLcad_item   15002 non-null  object
 8   ccbaAdmin_item  15002 non-null  object
 9   ccbaPoss_item   15002 non-null  object
 10  ccbaAsdt_item   15002 non-null  object
 11  ccbaCpno_item   15002 non-null  object
"""
