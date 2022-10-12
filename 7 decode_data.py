from utils.crawling import *

Ctcd_name = {"11": "서울", "21": "부산", "22": "대구", "23": "인천",  #4
             "24": "광주", "25": "대전", "26": "울산", "45": "세종",  #4
             "31": "경기", "32": "강원", "33": "충북", "34": "충남",  #4
             "35": "전북", "36": "전남", "37": "경북", "38": "경남", "50": "제주"}  #5
Pcd1_name = {"03": "석기", "05": "청동기", "07": "철기",  #3
             "11": "고구려", "12": "백제", "13": "신라", "14": "가야", "20": "통일신라",  #5
             "30": "고려", "40": "조선", "45": "대한제국", "50": "일제강점기"}  #4


heritage_df = csv_to_df("heritage.csv")

for i in range(len(heritage_df)):
    heritage_df.loc[i, "ccbaCtcdNm"] = Ctcd_name[heritage_df.loc[i, "ccbaCtcd"]]
    heritage_df.loc[i, "ccbaPcd1Nm"] = Pcd1_name[heritage_df.loc[i, "ccbaPcd1"]]

col = ['ccbaCpno', 'ccbaPcd1', 'ccbaPcd1Nm', 'longitude', 'latitude',
       'ccbaCtcd', 'ccbaCtcdNm', 'ccbaKdcd', 'ccmaName', 'crltsnoNm',
       'ccbaMnm1', 'ccbaMnm2', 'imageUrl', 'content', 'ccceName', 'ccbaLcad',
       'ccbaAdmin', 'ccbaPoss', 'ccbaAsdt']

save_df(heritage_df[col], "heritage.csv")
