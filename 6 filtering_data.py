from utils.filtering import *

heritage_df = csv_to_df("heritage_raw.csv", csv_raw_path)
heritage_df = filtering_df(heritage_df, filter)
heritage_df.columns = [col.split("_")[0] for col in heritage_df.columns]

save_df(heritage_df, "heritage.csv")
"""
RangeIndex: 1549 entries, 0 to 1548
Data columns (total 18 columns):
 #   Column     Non-Null Count  Dtype 
---  ------     --------------  ----- 
 0   ccbaCpno   1549 non-null   object
 1   ccbaPcd1   1549 non-null   object
 2   longitude  1549 non-null   object
 3   latitude   1549 non-null   object
 4   ccbaCtcd   1549 non-null   object
 5   ccbaLcto   1548 non-null   object
 6   ccbaKdcd   1549 non-null   object
 7   ccmaName   1549 non-null   object
 8   crltsnoNm  1549 non-null   object
 9   ccbaMnm1   1549 non-null   object
 10  ccbaMnm2   1548 non-null   object
 11  imageUrl   1549 non-null   object
 12  content    1549 non-null   object
 13  ccceName   1412 non-null   object
 14  ccbaLcad   1549 non-null   object
 15  ccbaAdmin  1549 non-null   object
 16  ccbaPoss   1549 non-null   object
 17  ccbaAsdt   1549 non-null   object
"""
