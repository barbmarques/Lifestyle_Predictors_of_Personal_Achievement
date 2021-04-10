import pandas as pd

def get_wellbeing_data():
    '''
    This function will download the dataset from the given url and write it to a pandas dataframe for use in exploration and modeling. 
    '''
    df = pd.read_csv(https://www.kaggle.com/ydalat/lifestyle-and-wellbeing-data?select=Wellbeing_and_lifestyle_data_Kaggle.csv)
    return df

  