import pandas as pd

from utils.crawling import *


Ctcd_name = {"11": "서울", "21": "부산", "22": "대구", "23": "인천", #4
             "24": "광주", "25": "대전", "26": "울산", "45": "세종", #4
             "31": "경기", "32": "강원", "33": "충북", "34": "충남", #4
             "35": "전북", "36": "전남", "37": "경북", "38": "경남", "50": "제주"} #5
Pcd1_name = {"03": "석기", "05": "청동기", "07": "철기", #3
             "11": "고구려", "12": "백제", "13": "신라", "14": "가야", "20": "통일신라", #5
             "30": "고려", "40": "조선", "45": "대한제국", "50": "일제강점기"} #4

heritage_df = csv_to_df("heritage.csv")
Ctcd_code_df = pd.DataFrame()
Lcto_code_df = pd.DataFrame()
Pcd1_code_df = pd.DataFrame()

for Ctcd in sorted(heritage_df["ccbaCtcd"].unique()):
    tmp = pd.DataFrame([[Ctcd, Ctcd_name[Ctcd]]], columns=["ccbaCtcd", "ccbaCtcdNm"])
    Ctcd_code_df = pd.concat([Ctcd_code_df, tmp], ignore_index=True)

    if Ctcd == "45":
        continue

    Lcto_df = csv_to_df(f"ccbaLcto_{Ctcd}.csv", ccbaLcto_path)

    for Lcto in sorted(heritage_df[heritage_df["ccbaCtcd"]==Ctcd]["ccbaLcto"].unique()):
        name = Lcto_df[Lcto_df["ccbaLcto_item"]==Lcto]["ccbaLctoNm_item"].iloc[0]
        tmp = pd.DataFrame([[Ctcd, Lcto, name]], columns=["ccbaCtcd", "ccbaLcto", "ccbaLctoNm"])
        Lcto_code_df = pd.concat([Lcto_code_df, tmp], ignore_index=True)


for Pcd1 in sorted(heritage_df["ccbaPcd1"].unique()):
    tmp = pd.DataFrame([[Pcd1, Pcd1_name[Pcd1]]], columns=["ccbaPcd1", "ccbaPcd1Nm"])
    Pcd1_code_df = pd.concat([Pcd1_code_df, tmp], ignore_index=True)

save_df(Ctcd_code_df, "Ctcd_code.csv")
save_df(Pcd1_code_df, "Pcd1_code.csv")
Lcto_code_df.to_csv("./data/Lcto_code.csv", encoding="utf-8-sig", index=True, index_label="id")