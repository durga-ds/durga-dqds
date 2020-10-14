# This function accepts a dataframe variable as input and selects data with columns from the dataframe 
# that have missing values. The result is assigned to another variable
#Example: Select from dataframe `df` columns that have missing values
#cols_with_nan = nan_cols(df)
#where cols_with_nan is of type pandas.core.frame.DataFrame

import pandas as pd
def nan_cols(df):
    null_list = []
    col_list = df.columns
    for c in col_list:
        if df[c].isnull().values.any():
            null_list.append(c)
    
    return df[null_list]