import numpy as np
import pandas as pd
# import seaborn as sns
# import matplotlib as plt
from sklearn.preprocessing import StandardScaler 
from sklearn.preprocessing import minmax_scale
import warnings
warnings.simplefilter('ignore')

def readData():

    df = pd.read_csv('C:\\Users\\tette\\Desktop\\PERSONAL\\STREAMLIT\\loanPg\\DataClass\\loan_data.csv')
    return df

def process_df(df):
    df['LoanAmount_log'] = np.log(df['LoanAmount'])

    df['LoanAmount_log'].hist(bins=20)

    df['Total_Income']=df['ApplicantIncome'] + df['CoapplicantIncome']

    df['Total_Income_log']=np.log(df['Total_Income'])

    df['Gender'].fillna(df['Gender'].mode()[0],inplace=True)
    df['Married'].fillna(df['Married'].mode()[0],inplace=True)
    df['Dependents'].fillna(df['Dependents'].mode()[0],inplace=True)
    df['Self_Employed'].fillna(df['Self_Employed'].mode()[0],inplace=True)
    df['LoanAmount'].fillna(df['LoanAmount'].mean(),inplace=True)
    df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0],inplace=True)
    df['Credit_History'].fillna(df['Credit_History'].mode()[0],inplace=True)
    df['LoanAmount_log'].fillna(df['LoanAmount_log'].mean(),inplace=True)

    from sklearn.preprocessing import LabelEncoder
    LabelEncoder_x = LabelEncoder()
    LabelEncoder_y = LabelEncoder()

    df['Gender']=LabelEncoder_x.fit_transform(df['Gender'])
    df['Married']=LabelEncoder_x.fit_transform(df['Married'])
    df['Education']=LabelEncoder_x.fit_transform(df['Education'])
    df['Loan_Status']=LabelEncoder_x.fit_transform(df['Loan_Status'])
    df['Self_Employed']=LabelEncoder_x.fit_transform(df['Self_Employed'])
    df['Property_Area']=LabelEncoder_x.fit_transform(df['Property_Area'])

    df['Dependents'] = df['Dependents'].replace('3+',3)

    from sklearn.model_selection import train_test_split
    y=df.iloc[:,12]
    X=df.iloc[:,[1,2,3, 4, 5, 9,10, 11,13,15]]

    # X=df.iloc[:,np.r_[1:5, 9:11,13:15]]
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)

    df['Dependents'] = df['Dependents'].astype(int)

    from sklearn.preprocessing import StandardScaler
    ss = StandardScaler()

    X_train = ss.fit_transform(X_train)
    from sklearn.tree import DecisionTreeClassifier
    dClf= DecisionTreeClassifier()

    dClf.fit(X_train,y_train)
    from sklearn import metrics
    y_pred = dClf.predict(X_test)
    a= dClf.predict([[1,1,2,0,0,360.0,5,2,50,8.675564]])

    return dClf