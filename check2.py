from utils_basic import *

pd.options.display.max_columns = None
pd.options.display.max_rows = None

info = csv_to_dataframe("info.csv")
period = csv_to_dataframe("period.csv")

df = pd.merge(left=info, right=period, on=PK, how="outer")

# print(df["ccbaPcd1_item"].value_counts().sort_index())

for item in ["01", "03", "05", "07", "10", "11", "12", "13", "14", "20"]:
    print("="*50)
    print(df[df["ccbaPcd1_item"]==item][["ccceName_item", "ccbaMnm1_item"]])
