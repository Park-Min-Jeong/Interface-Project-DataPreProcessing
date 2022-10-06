import pandas as pd

from utils_basic import *


def filter_location_period():
    location_period = pd.merge(left=csv_to_dataframe("location_raw.csv", csv_raw_path),
                               right=csv_to_dataframe("period_raw.csv", csv_raw_path),
                               on=PK, how="outer")

    # conditions
    c1 = location_period["ccbaPcd1_item"].isnull()  # 시대가 결측값
    c2 = location_period["ccbaPcd1_item"] == "60"  # 시대가 미상
    c3 = location_period["ccbaPcd1_item"] == "00"  # 시대가 선사시대 이전
    c4 = location_period["longitude_item"] == "0"  # 경도가 결측값
    c5 = location_period["latitude_item"] == "0"  # 위도가 결측값
    condition = c1 | c2 | c3 | c4 | c5

    return location_period[condition][PK]


def filter_info():
    info = csv_to_dataframe("info_raw.csv", csv_raw_path)
    result = pd.DataFrame(columns=info.columns)
    for i in range(len(info)):
        row = info.loc[i, :]

        if type(row["ccbaLcad_item"])==str:
            if "박물관" in row["ccbaLcad_item"] or "미술관" in row["ccbaLcad_item"]:
                result = pd.concat([result, pd.DataFrame([row], columns=info.columns)], ignore_index=True)

    return result[PK]


def filter_kind():
    kind = csv_to_dataframe("kind_raw.csv", csv_raw_path)
    remain_list = ["11", "12", "13"]
    result = pd.DataFrame(columns=kind.columns)
    for i in range(len(kind)):
        row = kind.loc[i, :]

        if row["ccbaKdcd_item"] not in remain_list:
            result = pd.concat([result, pd.DataFrame([row], columns=kind.columns)], ignore_index=True)

    return result[PK]


def making_filter():
    filter1 = filter_location_period()
    filter2 = filter_info()
    filter3 = filter_kind()
    filter_df = pd.concat([filter1, filter2], ignore_index=True)
    filter_df = pd.concat([filter_df, filter3], ignore_index=True)
    filter = filter_df.unique()

    return filter


def filtering(df, filter):
    for i in range(len(df)):
        if df.loc[i, PK] in filter:
            df = df.drop(index=i)

    df = df.reset_index(drop=True)
    print(len(df))

    return df

filter = making_filter()
