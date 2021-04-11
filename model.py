import pandas as pd
import sklearn
from sklearn import preprocessing
# #Modeling Imports
from sklearn.model_selection import learning_curve
from sklearn.cluster import KMeans, dbscan
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import SelectKBest, RFE, f_regression 
from sklearn.linear_model import LinearRegression, LassoLars
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import MinMaxScaler

def split_target(train, validate, test):
    
    X_train = train.drop(columns=['achievement','high_ach'])
    X_validate = validate.drop(columns=['achievement','high_ach'])
    X_test = test.drop(columns=['achievement','high_ach'])
    y_train = train[['achievement']]
    y_validate = validate[['achievement']]
    y_test = test[['achievement']]

    print(f'X_train -> {X_train.shape}')
    print(f'X_validate -> {X_validate.shape}')
    print(f'X_test -> {X_test.shape}')
    print(f'y_train -> {y_train.shape}')
    print(f'y_validate -> {y_validate.shape}')
    print(f'y_test -> {y_test.shape}')
    
    return X_train, X_validate, X_test, y_train, y_validate, y_test



def min_max_scale(X_train, X_validate, X_test, numeric_cols):
    '''
    this function takes in 3 dataframes with the same columns, 
    a list of numeric column names (because the scaler can only work with numeric columns),
    and fits a min-max scaler to the first dataframe and transforms all
    3 dataframes using that scaler. 
    it returns 3 dataframes with the same column names and scaled values. 
    '''
    # create the scaler object and fit it to X_train (i.e. identify min and max)
    # if copy = false, inplace row normalization happens and avoids a copy (if the input is already a numpy array).


    scaler = MinMaxScaler(copy=True).fit(X_train[numeric_cols])

    #scale X_train, X_validate, X_test using the mins and maxes stored in the scaler derived from X_train. 
    # 
    X_train_scaled_array = scaler.transform(X_train[numeric_cols])
    X_validate_scaled_array = scaler.transform(X_validate[numeric_cols])
    X_test_scaled_array = scaler.transform(X_test[numeric_cols])

    # convert arrays to dataframes
    X_train_scaled = pd.DataFrame(X_train_scaled_array, 
                                  columns=numeric_cols).\
                                  set_index([X_train.index.values])

    X_validate_scaled = pd.DataFrame(X_validate_scaled_array, 
                                     columns=numeric_cols).\
                                     set_index([X_validate.index.values])

    X_test_scaled = pd.DataFrame(X_test_scaled_array, 
                                 columns=numeric_cols).\
                                 set_index([X_test.index.values])

    
    return X_train_scaled, X_validate_scaled, X_test_scaled



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~from sklearn.feature_selection import SelectKBest, f_regression

def select_kbest(X_train_scaled, y_train, k, target): 

    '''
    This function takes in a list of independent variables, or predictors (x), the target
    variable (y) and the number of features to select (k), fits  X_train_scaled and returns
    (prints) the names of the top k selected ffeatures based on the SelectKBest class.
    ''' 

    # parameters: f_regression stats test, return k number of features
    f_selector = SelectKBest(f_regression, k=k)

    # find the top k X's correlated with y
    f_selector.fit(X_train_scaled, y_train)

    # boolean mask of whether the column was selected or not. 
    feature_mask = f_selector.get_support()
    
    # get list of top K features. 
    f_feature = X_train_scaled.iloc[:,feature_mask].columns.tolist()
    
    print(f'The {k} best predictors of {target}, according to k best are: {f_feature}.')
    return
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def rfe(X_train_scaled, y_train, k, target): 
    
    '''
    This function takes in a list of independent variables, or predictors (x), the target
    variable (y) and the number of features to select (k), fits X_train_scaled
    and returns (prints) the names of the top k selected features based on the RFE class.
    ''' 

    # initialize the ML algorithm
    lm = LinearRegression()

    # create the rfe object, indicating the ML object (lm) and the number of features I want to end up with. 
    rfe = RFE(lm, k)

    # fit the data using RFE
    rfe.fit(X_train_scaled,y_train)  

    # get the mask of the columns selected
    feature_mask = rfe.support_

    # get list of the column names. 
    rfe_feature = X_train_scaled.iloc[:,feature_mask].columns.tolist()

    print(f'The {k} best predictors of {target}, according to recursive feature elimination are: {rfe_feature}.')
