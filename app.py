import streamlit as st
import pandas as pd
import joblib
from src.predict import predict

st.title("Loan Approval Prediction System")

st.write("Enter applicant details below")

Gender = st.selectbox("Gender", ["Male","Female"])
Married = st.selectbox("Married", ["Yes","No"])
Dependents = st.selectbox("Dependents", ["0","1","2","3+"])
Education = st.selectbox("Education", ["Graduate","Not Graduate"])
Self_Employed = st.selectbox("Self Employed", ["Yes","No"])

ApplicantIncome = st.number_input("Applicant Income")
CoapplicantIncome = st.number_input("Coapplicant Income")
LoanAmount = st.number_input("Loan Amount")
Loan_Amount_Term = st.number_input("Loan Amount Term")

Credit_History = st.selectbox("Credit History", [1,0])
Property_Area = st.selectbox("Property Area", ["Urban","Semiurban","Rural"])


if st.button("Predict Loan Status"):

    input_data = {
        "Gender": Gender,
        "Married": Married,
        "Dependents": Dependents,
        "Education": Education,
        "Self_Employed": Self_Employed,
        "ApplicantIncome": ApplicantIncome,
        "CoapplicantIncome": CoapplicantIncome,
        "LoanAmount": LoanAmount,
        "Loan_Amount_Term": Loan_Amount_Term,
        "Credit_History": Credit_History,
        "Property_Area": Property_Area
    }

    prediction = predict(input_data)

    if prediction == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")