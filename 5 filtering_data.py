from utils_filter import *


for name in ["period", "location", "name", "region", "kind", "info"]:
    csv_name = name + "_raw.csv"

    df = csv_to_dataframe(csv_name, csv_raw_path)
    df = filtering(df, filter)
    save_df(df, name+".csv")

"""
=== period.csv ===
RangeIndex: 1549 entries, 0 to 1548
Data columns (total 2 columns):
 #   Column         Non-Null Count  Dtype 
---  ------         --------------  ----- 
 0   ccbaCpno_item  1549 non-null   object
 1   ccbaPcd1_item  1549 non-null   object
 
 === location.csv ===
RangeIndex: 1549 entries, 0 to 1548
Data columns (total 3 columns):
 #   Column          Non-Null Count  Dtype 
---  ------          --------------  ----- 
 0   ccbaCpno_item   1549 non-null   object
 1   longitude_item  1549 non-null   object
 2   latitude_item   1549 non-null   object
 
 === name.csv ===
RangeIndex: 1549 entries, 0 to 1548
Data columns (total 2 columns):
 #   Column         Non-Null Count  Dtype 
---  ------         --------------  ----- 
 0   ccbaCpno_item  1549 non-null   object
 1   ccbaMnm1_item  1549 non-null   object
 
 === region.csv ===
RangeIndex: 1549 entries, 0 to 1548
Data columns (total 3 columns):
 #   Column         Non-Null Count  Dtype 
---  ------         --------------  ----- 
 0   ccbaCpno_item  1549 non-null   object
 1   ccbaCtcd_item  1549 non-null   object
 2   ccbaLcto_item  1548 non-null   object
 
 === kind.csv ===
RangeIndex: 1549 entries, 0 to 1548
Data columns (total 2 columns):
 #   Column         Non-Null Count  Dtype 
---  ------         --------------  ----- 
 0   ccbaCpno_item  1549 non-null   object
 1   ccbaKdcd_item  1549 non-null   object
 
 === info.csv ===
RangeIndex: 1549 entries, 0 to 1548
Data columns (total 12 columns):
 #   Column          Non-Null Count  Dtype 
---  ------          --------------  ----- 
 0   ccmaName_item   1549 non-null   object
 1   crltsnoNm_item  1549 non-null   object
 2   ccbaMnm1_item   1549 non-null   object
 3   ccbaMnm2_item   1548 non-null   object
 4   imageUrl_item   1549 non-null   object
 5   content_item    1549 non-null   object
 6   ccceName_item   1412 non-null   object
 7   ccbaLcad_item   1549 non-null   object
 8   ccbaAdmin_item  1549 non-null   object
 9   ccbaPoss_item   1549 non-null   object
 10  ccbaAsdt_item   1549 non-null   object
 11  ccbaCpno_item   1549 non-null   object
"""
