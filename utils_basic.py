from urllib import request
from bs4 import BeautifulSoup
import pandas as pd


def making_columns(find_list, add_dict):
    # parsing_raw_xml() & parsing_xml()
    col_list = list()
    for tag in find_list + list(add_dict.keys()):
        col_list.append(f"{tag}_item")

    return col_list


def making_url(url, params):
    # making_raw_df() & making_df()
    for k, v in params.items():
        url = url + f"&{k}={v}"

    return url


def making_add_dict(add_list, params):
    # making_raw_df() & making_df()
    add_dict = dict()
    for k, v in params.items():
        if k in add_list:
            add_dict[k] = v

    return add_dict


def csv_to_dataframe(name, path="./data/"):
    df = pd.read_csv(path+name, encoding="utf-8-sig", dtype="object")
    return df


def save_df(df, name, path="./data/"):
    print(df.info())

    if "raw" in name:
        path = csv_raw_path

    df.to_csv(path+name, encoding="utf-8-sig", index=False)


s_url = "http://www.cha.go.kr/cha/SearchKindOpenapiList.do?ccbaCncl=N&pageUnit=20000"
sd_url = "http://www.cha.go.kr/cha/SearchKindOpenapiDt.do?"

PK = "ccbaCpno_item"

csv_raw_path = "./data/raw/"