from utils.filtering import *

heritage_df = csv_to_df("heritage_raw.csv", csv_raw_path)

# filtering
heritage_df = filtering_df(heritage_df, filter)
heritage_df.columns = [col.split("_")[0] for col in heritage_df.columns]

# modifying
condition = pd.read_csv("./data/modify_period.csv", encoding="utf-8")
heritage_df = pd.merge(left=condition, right=heritage_df, on="ccbaMnm1", how="outer").drop("index", axis=1)

values = {"석기":"03", "청동기":"05", "철기시대":"07",
          "고구려":"11", "백제":"12", "신라":"13", "가야":"14",
          "통일신라":"20", "고려":"30"}

for i in range(len(heritage_df)):
    row = heritage_df.iloc[i, :]
    if row["ccbaPcd1"] == "01" or row["ccbaPcd1"]=="10":
        heritage_df.loc[i, "ccbaPcd1"] = values[row["period"]]

heritage_df = heritage_df.drop("period", axis=1)

save_df(heritage_df, "heritage.csv")
"""
Int64Index: 1328 entries, 0 to 1327
Data columns (total 18 columns):
 #   Column     Non-Null Count  Dtype 
---  ------     --------------  ----- 
 0   ccbaMnm1   1328 non-null   object
 1   ccbaCpno   1328 non-null   object
 2   ccbaPcd1   1328 non-null   object
 3   longitude  1328 non-null   object
 4   latitude   1328 non-null   object
 5   ccbaCtcd   1328 non-null   object
 6   ccbaLcto   1327 non-null   object
 7   ccbaKdcd   1328 non-null   object
 8   ccmaName   1328 non-null   object
 9   crltsnoNm  1328 non-null   object
 10  ccbaMnm2   1327 non-null   object
 11  imageUrl   1328 non-null   object
 12  content    1328 non-null   object
 13  ccceName   1216 non-null   object
 14  ccbaLcad   1328 non-null   object
 15  ccbaAdmin  1328 non-null   object
 16  ccbaPoss   1328 non-null   object
 17  ccbaAsdt   1328 non-null   object
"""
