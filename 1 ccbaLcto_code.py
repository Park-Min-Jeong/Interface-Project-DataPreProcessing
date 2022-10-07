from utils.crawling import *

ccbaCtcd_list = ["11", "21", "22", "23", "24", "25", "26", "45",
                 "31", "32", "33", "34", "35", "36", "37", "38",
                 "50"
]
find_list = ["ccbaLcto", "ccbaLctoNm"]
add_list = []

for Ctcd in ccbaCtcd_list:
    df = crawling_process(l_url, find_list, add_list, ccbaCtcd=Ctcd)
    save_df(df, f"ccbaLcto_{Ctcd}.csv")
