import pandas as pd
import numpy as np

def load_and_process(path_to_csv):
    
    df1 = (
        pd.read_csv(path_to_csv)
        .drop(['ORI', 'PUB_AGENCY_NAME', 'PUB_AGENCY_UNIT', 'AGENCY_TYPE_NAME', 'STATE_ABBR', 'POPULATION_GROUP_CODE', 'OFFENSE_CODE', 'VICTIM_TYPE_CODE', 'LOCATION_CODE', 'WEAPON_CODE', 'PROP_DESC_ID', 'PROP_DESC_CODE'], axis=1)
    )
    
    
    return df1

df = load_and_process("../../Dataset.csv")
print(df)