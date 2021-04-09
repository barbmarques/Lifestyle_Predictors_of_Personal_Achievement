import pandas as pd
from pandas import DataFrame
from sklearn.model_selection import train_test_split

def prep_wellbeing(df):
    '''
    prep_wellbeing will take in the wellbeing dataframe acquired as df and remove any null values, rename columns to more user-friendly titles and
    remove columns that are not relevant to our immediate analysis of the data
    
    A single, cleaned dataframe will be returned, ready for exploration and testing.
    '''
    df.drop_duplicates
    
    dropcols = ['Timestamp', 'SUFFICIENT_INCOME']
    df.drop(columns=dropcols, inplace = True)
   
    df = df.rename(columns={'FRUITS_VEGGIES': 'diet','BMI_RANGE':'bmi', 'SLEEP_HOURS':'sleep_hours', 'AGE':'age_range', 'GENDER':'is_female', 'DONATION':'donation'})
   
    return df


def train_validate_test_split(df, seed=123):
    train_and_validate, test = train_test_split(
        df, test_size=0.2, random_state=seed, stratify=None
    )
    train, validate = train_test_split(
        train_and_validate,
        test_size=0.3,
        random_state=seed,
        stratify=train_and_validate
    )
    return train, validate, test
