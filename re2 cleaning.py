from utils.re_utils import *

raw_df = csv_to_df("re_raw.csv", csv_raw_path)

# removing conditions
c1 = raw_df["ccbaPcd1_item"] == "60"  # 시대가 미상
c2 = raw_df["ccbaPcd1_item"] == "00"  # 시대가 선사시대 이전
c3 = raw_df["longitude_item"] == "0"  # 경도가 결측값
c4 = raw_df["latitude_item"] == "0"  # 위도가 결측값
c5 = raw_df[["longitude_item", "latitude_item"]].duplicated(keep=False)  # 경도와 위도가 중복됨
c6 = ~raw_df["ccbaKdcd_item"].isin(["11", "12", "13"])  # 국보, 보물, 사적이 아님
conditions = c1 | c2 | c3 | c4 | c5 | c6
df = raw_df[~conditions].reset_index(drop=True)

# change data type
df = df.astype({"longitude_item": float,
                "latitude_item": float})

# modify ccbaPcd1
m = csv_to_df("re_modify_period.csv")
periods = {name: period for name, period in zip(m["name"], m["period"])}
for i in range(len(df)):
    if df.loc[i, "ccbaPcd1_item"] in ["01", "10"]:
        df.loc[i, "ccbaPcd1_item"] = periods[df.loc[i, "ccbaMnm1_item"]]

df["ccbaPcd1_item"] = df.apply(lambda row:
                               periods[row["ccbaMnm1_item"]] if row["ccbaPcd1_item"] in ["01", "10"]
                               else row["ccbaPcd1_item"], axis=1)

# make ccbaPcd1Nm
df["ccbaPcd1Nm_item"] = df["ccbaPcd1_item"].replace(Pcd1_name)

# change column names
df.columns = [col.split("_")[0] for col in df.columns]

save_df(df, "re_heritage.csv")
"""
RangeIndex: 1338 entries, 0 to 1337
Data columns (total 15 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   ccbaCpno    1338 non-null   object 
 1   ccbaKdcd    1338 non-null   object 
 2   ccmaName    1338 non-null   object 
 3   crltsnoNm   1338 non-null   object 
 4   ccbaMnm1    1338 non-null   object 
 5   ccbaMnm2    1337 non-null   object 
 6   ccbaCtcd    1338 non-null   object 
 7   ccbaCtcdNm  1338 non-null   object 
 8   ccsiName    1337 non-null   object 
 9   ccbaAdmin   1338 non-null   object 
 10  ccbaAsno    1338 non-null   object 
 11  longitude   1338 non-null   float64
 12  latitude    1338 non-null   float64
 13  ccbaPcd1    1338 non-null   object 
 14  ccbaPcd1Nm  1338 non-null   object 
"""