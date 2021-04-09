import pandas as pd

def get_wellbeing_data():
    '''
    This function will pull the dataset from the provided .csv file and will write it to a pandas dataframe for use in exploration and modeling. 
    If you want to reproduce the results, you will need the Wellbeing_Lifestyle.csv file in your working directory.
    '''
    df = pd.read_csv('Wellbeing_Lifestyle.csv')  
    return df

  