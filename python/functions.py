import pandas as pd
import numpy as np

def check_null_inf(df):
    print("Null value counts:")
    print(df.isnull().sum())
    
    print("\nInfinite value counts:")
    for column in df.columns:
        if np.issubdtype(df[column].dtype, np.number):
            print(f"In '{column}' column:", np.isinf(df[column]).sum())