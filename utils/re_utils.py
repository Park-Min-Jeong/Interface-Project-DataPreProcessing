from urllib import request
from bs4 import BeautifulSoup
import pandas as pd


def csv_to_df(name, path="./data/"):
    if "raw" in name:
        path = csv_raw_path

    df = pd.read_csv(path+name, encoding="utf-8-sig", dtype="object")
    return df


def save_df(df, name, path="./data/"):
    print(df.info())

    if "raw" in name:
        path = csv_raw_path

    df.to_csv(path+name, encoding="utf-8-sig", index=False)


def making_url(url, params):
    for k, v in params.items():
        url = url + f"&{k}={v}"

    return url


def parsing_xml(url, find_list, params):
    # find_list: response parameters
    # params: request parameters
    result = request.urlopen(url)
    soup = BeautifulSoup(result, "lxml-xml")

    # making column list
    col_list = [f"{x}_item" for x in find_list + list(params.keys())]

    df = pd.DataFrame(columns=col_list)

    # parsing item tag
    items = soup.find_all("item")
    for item in items:
        item_list = list()
        # result of response parameters
        for tag in find_list:
            tag_item = item.find(tag).string
            if tag_item:
                tag_item = tag_item.replace("\n", "").replace("\t", "").strip()
            item_list.append(tag_item)
        # result of request parameters
        for value in params.values():
            item_list.append(value)
        # appending to dataframe
        df = pd.concat([df, pd.DataFrame([item_list], columns=col_list)], ignore_index=True)
    return df


def crawling_process(API, find_list, **params):
    url = making_url(API, params)

    df = parsing_xml(url, find_list, params)

    if len(df) == 0:
        print(f"{url} -- ERROR")
    else:
        print(f"{url} -- {len(df)}")

    return df


API = "http://www.cha.go.kr/cha/SearchKindOpenapiList.do?ccbaCncl=N&pageUnit=20000"

csv_raw_path = "./data/raw/"

Pcd1_name = {"03": "석기", "05": "청동기", "07": "철기",
             "11": "고구려", "12": "백제", "13": "신라", "14": "가야", "20": "통일신라",
             "30": "고려", "40": "조선", "45": "대한제국", "50": "일제강점기"}