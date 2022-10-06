from utils_basic import *

pd.options.display.max_columns = None
pd.options.display.max_rows = None

# location_df = csv_to_dataframe("location_raw.csv", csv_raw_path)
# info_df = csv_to_dataframe("info_raw.csv", csv_raw_path)
location_df = csv_to_dataframe("location.csv")
info_df = csv_to_dataframe("info.csv")

df = pd.merge(left=location_df, right=info_df, on=PK, how="outer")

# print(df[["longitude_item", "latitude_item"]].duplicated(keep=False).value_counts())

duplicate_df = df[df[["longitude_item", "latitude_item"]].duplicated(keep=False)][["longitude_item", "latitude_item", "ccbaLcad_item", "ccbaMnm1_item"]]

grouped_df = duplicate_df.groupby(["longitude_item", "latitude_item"])

for key, item in grouped_df:
    print(grouped_df.get_group(key), "\n\n")
