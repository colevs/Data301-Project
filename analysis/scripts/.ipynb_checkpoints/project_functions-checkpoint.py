import pandas as pd
import numpy as np

def load_and_process(path_to_csv):
    
    df1 = (
        pd.read_csv(path_to_csv)
        #.drop([], axis=1)
    )
    
    
    return df1

df = load_and_process("..//..//Dataset.xlsx")
print(df)