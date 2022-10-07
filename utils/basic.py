from utils.variables import *


def making_columns(find_list, add_dict):
    col_list = list()
    for tag in find_list + list(add_dict.keys()):
        col_list.append(f"{tag}_item")

    return col_list


def making_url(url, params):
    for k, v in params.items():
        url = url + f"&{k}={v}"

    return url


def making_add_dict(add_list, params):
    add_dict = dict()
    for k, v in params.items():
        if k in add_list:
            add_dict[k] = v

    return add_dict


def csv_to_df(name, path="./data/"):
    df = pd.read_csv(path+name, encoding="utf-8-sig", dtype="object")
    return df


def merge_df(df1, df2):
    return pd.merge(left=df1, right=df2, on=PK, how="outer")


def save_df(df, name, path="./data/"):
    print(df.info())

    if "raw" in name:
        path = csv_raw_path
    elif "Lcto" in name:
        path = ccbaLcto_path

    df.to_csv(path+name, encoding="utf-8-sig", index=False)