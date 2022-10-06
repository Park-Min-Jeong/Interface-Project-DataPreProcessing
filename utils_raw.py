from utils_basic import *


def parsing_xml(url, find_list, add_dict):
    # find_list: response parameters
    # add_dict: request parameters

    result = request.urlopen(url)
    soup = BeautifulSoup(result, "lxml-xml")

    # making column list
    col_list = making_columns(find_list, add_dict)

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
        for value in add_dict.values():
            item_list.append(value)
        # appending to dataframe
        df = pd.concat([df, pd.DataFrame([item_list], columns=col_list)], ignore_index=True)

    # parsing ccbaCpno tag
    # for detail search: ccbaCpno 태그가 item 태그 밖에 존재
    if "Dt" in url:
        df["ccbaCpno_item"] = [soup.find("ccbaCpno").string]

    return df


def crawling_process(url, find_list, add_list, **params):
    url = making_url(url, params)
    add_dict = making_add_dict(add_list, params)

    df = parsing_xml(url, find_list, add_dict)

    if len(df)==0:
        print(f"{url} -- ERROR")
    else:
        print(f"{url} -- {len(df)}")

    return df