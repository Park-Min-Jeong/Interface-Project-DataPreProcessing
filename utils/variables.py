from urllib import request
from bs4 import BeautifulSoup
import pandas as pd

l_url = "https://www.cha.go.kr/common/heritage/selectSearchGugunCdOpenApi.jsp?"
s_url = "http://www.cha.go.kr/cha/SearchKindOpenapiList.do?ccbaCncl=N&pageUnit=20000"
sd_url = "http://www.cha.go.kr/cha/SearchKindOpenapiDt.do?"


PK = "ccbaCpno_item"

ccbaLcto_path = "./data/ccbaLcto/"
csv_raw_path = "./data/raw/"