"""
heritage_raw.csv
"""

from utils.basic import *

name_list = ["period", "location", "region", "kind", "info"]

df_merge = pd.DataFrame(columns=[PK])

for name in name_list:
    csv_name = name + "_raw.csv"
    df_merge = merge_df(df_merge, csv_to_df(csv_name, csv_raw_path))

save_df(df_merge, "heritage_raw.csv")
"""
Int64Index: 15002 entries, 0 to 15001
Data columns (total 18 columns):
 #   Column          Non-Null Count  Dtype 
---  ------          --------------  ----- 
 0   ccbaCpno_item   15002 non-null  object
 1   ccbaPcd1_item   8922 non-null   object
 2   longitude_item  15002 non-null  object
 3   latitude_item   15002 non-null  object
 4   ccbaCtcd_item   14983 non-null  object
 5   ccbaLcto_item   14832 non-null  object
 6   ccbaKdcd_item   15002 non-null  object
 7   ccmaName_item   15002 non-null  object
 8   crltsnoNm_item  15002 non-null  object
 9   ccbaMnm1_item   15002 non-null  object
 10  ccbaMnm2_item   13847 non-null  object
 11  imageUrl_item   14700 non-null  object
 12  content_item    14678 non-null  object
 13  ccceName_item   7307 non-null   object
 14  ccbaLcad_item   14899 non-null  object
 15  ccbaAdmin_item  13854 non-null  object
 16  ccbaPoss_item   14147 non-null  object
 17  ccbaAsdt_item   15002 non-null  object
"""