from urllib import request
from bs4 import BeautifulSoup
import pandas as pd

ccbaCtcd = ["11", "21", "22", "23", "24", "25", "26", "45",
            "31", "32", "33", "34", "35", "36", "37", "38",
            "50"]

for code in ccbaCtcd:
    url = f"https://www.cha.go.kr/common/heritage/selectSearchGugunCdOpenApi.jsp?ccbaCtcd={code}"

    result = request.urlopen(url)
    soup = BeautifulSoup(result, "lxml-xml")

    items = soup.find_all("item")

    df = pd.DataFrame(columns=["num", "region"])

    for item in items:
        temp_df = pd.DataFrame([[str(item.find("ccbaLcto").string), item.find("ccbaLctoNm").string]],
                               columns=["num", "region"])
        df = pd.concat([df, temp_df], ignore_index=True)

    df.to_csv(f"./ccbaLcto/ccbaLcto_{code}.csv", index=False, encoding="utf-8-sig")

