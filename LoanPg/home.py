import streamlit as st
import time

st.title(''':orange[LOAN PREDICTION APP]''')
from DataClass.loan import readData, process_df

st.text('Please provide information in the form below to give you an idea')
st.text( 'of your chances of getting approved for a loan')

with st.form('My Prediction Form'):
# Gender	Married	Dependents	Education	Self_Employed	LoanAmount	
# Loan_Amount_Term	Credit_History	Property_Area	Total_Income
    gender = st.selectbox('Gender',['Male','Female'])
    married = st.selectbox('Married',['Yes','No'])
    dependents = st.selectbox('Dependents',['0','1','2','3+'])
    education = st.selectbox('Education',['Graduate','Not Graduate'])
    self_employed = st.selectbox('Self_Employed',['Yes','No'])
    loan_term = st.number_input('Enter your estimated Loan term(in months)',min_value=2, max_value= 600)
    credit_history = st.selectbox('Do you have credit history?',['Yes','No'])
    property_area = st.selectbox('Where is your property located?',['Urban','Rural','Semiurban'])
    loan_amount = st.number_input('Enter your desired loan amount(in thousands 000)',min_value=2, max_value= 500)
    total_income = st.number_input('Enter your monthly income',min_value=200, max_value=10000000)
    submit = st.form_submit_button('Predict ','Click to predict') 


    if submit:
        df = readData()
        model = process_df(df)
        gender = 0
        if gender == 'Male':
            gender = 1
        else:
            gender = 0

        married = 0
        if married == 'Yes':
            married = 1
        else:
            married = 0

        dependents = 0
        if dependents == '0':
            dependents = 0
        elif dependents == '1':
            dependents = 1
        elif dependents == '2':
            dependents = 2
        else:
            dependents = 3

        education = 0
        if education == 'Graduate':
            education = 1
        else:
            education = 0

        self_employed = 0
        if self_employed == 'Yes':
            self_employed = 1
        else:
            self_employed = 0

        credit_history = 0
        if credit_history == 'Yes':
            credit_history = 1
        else:
            credit_history = 0

        property_area = 0
        if property_area == 'Urban':
            property_area = 2
        elif property_area == 'Rural':
            property_area = 0
        else:
            property_area = 1
        
        # Gender	Married	Dependents	Education	Self_Employed	LoanAmount	
# Loan_Amount_Term	Credit_History	Property_Area	Total_Income
        
        result = model.predict([[gender,married,dependents,education,self_employed,loan_amount
                                 ,loan_term, credit_history, property_area, total_income]]) 
        
        st.write("---")
        with st.spinner('Wait for it...'):
            time.sleep(2)
            st.success('Done!')
        if result==0:
            st.markdown('''You are :orange[preapproved] for the this loan based on the information provided''')
        else:
            st.markdown('''You orange:[do not qualify] for the this loan based on the information provided''')
