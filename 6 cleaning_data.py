from utils.filtering import *
from utils.modifying import *

heritage_df = csv_to_df("heritage_raw.csv", csv_raw_path)

heritage_df = filtering_df(heritage_df, filter)
heritage_df = modifying_df(heritage_df)

save_df(heritage_df, "heritage.csv")
"""
Int64Index: 1328 entries, 0 to 1327
Data columns (total 18 columns):
 #   Column     Non-Null Count  Dtype 
---  ------     --------------  ----- 
 0   ccbaMnm1   1328 non-null   object
 1   ccbaCpno   1328 non-null   object
 2   ccbaPcd1   1328 non-null   object
 3   longitude  1328 non-null   object
 4   latitude   1328 non-null   object
 5   ccbaCtcd   1328 non-null   object
 6   ccbaLcto   1327 non-null   object
 7   ccbaKdcd   1328 non-null   object
 8   ccmaName   1328 non-null   object
 9   crltsnoNm  1328 non-null   object
 10  ccbaMnm2   1327 non-null   object
 11  imageUrl   1328 non-null   object
 12  content    1328 non-null   object
 13  ccceName   1216 non-null   object
 14  ccbaLcad   1328 non-null   object
 15  ccbaAdmin  1328 non-null   object
 16  ccbaPoss   1328 non-null   object
 17  ccbaAsdt   1328 non-null   object
"""
