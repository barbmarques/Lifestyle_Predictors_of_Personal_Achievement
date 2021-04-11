import pandas as pd
import numpy as np
from pandas import DataFrame
from sklearn.model_selection import train_test_split

def prep_wellbeing(df):
    '''
    prep_wellbeing will take in the wellbeing dataframe acquired as df and remove any null 
    values, change datatype of stress rating, rename columns to more user-friendly titles and 
    remove columns that are not relevant to our immediate analysis of the data.
    
    A single, cleaned dataframe will be returned, ready for exploration and testing.
    '''
    df.drop_duplicates
    
    dropcols = ['Timestamp', 
                'SUFFICIENT_INCOME', 
                'TODO_COMPLETED', 
                'LOST_VACATION', 
                'FLOW', 
                'PLACES_VISITED'
                ]
    
    df.drop(columns=dropcols, inplace = True)
    
    index_stress = df.loc[df.DAILY_STRESS == '1/1/00'].index
    df.drop(index_stress, inplace = True)
            
    df = df.rename(columns={'BMI_RANGE':'bmi', 
                            'SLEEP_HOURS':'sleep_hrs', 
                            'AGE':'age_range', 
                            'GENDER':'gender', 
                            'DONATION':'donation', 
                            'DAILY_STRESS':'stress',
                            'PLACES_VISITED':'new_places', 
                            'CORE_CIRCLE':'core_circle', 
                            'SUPPORTING_OTHERS':'support', 
                            'SOCIAL_NETWORK':'social', 
                            'WEEKLY_MEDITATION':'meditation',
                            'WORK_LIFE_BALANCE_SCORE':'balance',
                            'ACHIEVEMENT':'achievement',
                            'PERSONAL_AWARDS':'awards',
                            'DAILY_STEPS':'steps', 
                            'DAILY_SHOUTING':'shouts',
                            'TIME_FOR_PASSION':'passion',
                            'FRUITS_VEGGIES':'fruit_veg',
                            'LIVE_VISION':'vision'
                            })
    

    df['stress'] = df['stress'].astype('int')

    return df




def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test

