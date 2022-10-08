from utils.basic import *


def modifying_Pcd1(df):
    modify = csv_to_df("modify_period.csv")
    tmp = merge_df(modify, df, "ccbaMnm1_item").drop("index", axis=1)

    values = {
        "석기": "03", "청동기": "05", "철기시대": "07",
              "고구려": "11", "백제": "12", "신라": "13", "가야": "14",
              "통일신라": "20", "고려": "30"
    }

    col = "ccbaPcd1_item"
    for i in range(len(tmp)):
        row = tmp.iloc[i, :]
        if row[col] == "01" or row[col] == "10":
            tmp.loc[i, col] = values[row["period"]]

    return tmp.drop("period", axis=1)


def modifying_Asdt(df):
    df["ccbaAsdt_item"] = pd.to_datetime(df["ccbaAsdt_item"]).dt.date

    return df


def modifying_column(df):
    df.columns = [col.split("_")[0] for col in df.columns]

    column_order = [
        "ccbaCpno", "ccbaPcd1", "longitude", "latitude",
        "ccbaCtcd", "ccbaLcto", "ccbaKdcd", "ccmaName", "crltsnoNm",
        "ccbaMnm1", "ccbaMnm2", "imageUrl", "content",
        "ccceName", "ccbaLcad", "ccbaAdmin", "ccbaPoss", "ccbaAsdt"
    ]

    return df[column_order]


def modifying_df(df):
    df = modifying_Pcd1(df)
    df = modifying_Asdt(df)
    df = modifying_column(df)

    return df