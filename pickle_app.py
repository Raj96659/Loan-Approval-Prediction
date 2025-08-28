import streamlit as st
import pickle
import numpy as np

# Load pickled model and scaler
model = pickle.load(open('logistic.pkl', 'rb'))
scaler = pickle.load(open('log_scale.pkl', 'rb'))

# App title
st.title("Loan Approval Prediction")

st.write("Enter applicant details to predict loan approval:")

# Input fields
gender = st.selectbox("Gender", ["Female", "Male"])
married = st.selectbox("Married", ["No", "Yes"])
dependents = st.number_input("Dependents", min_value=0, max_value=10, step=1)
education = st.selectbox("Education", ["Not Graduate", "Graduate"])
self_employed = st.selectbox("Self Employed", ["No", "Yes"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_amount_term = st.number_input("Loan Amount Term (months)", min_value=0)
credit_history = st.selectbox("Credit History", [0, 1])
property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

# Encode categorical features
gender_enc = 1 if gender == "Male" else 0
married_enc = 1 if married == "Yes" else 0
education_enc = 1 if education == "Graduate" else 0
self_employed_enc = 1 if self_employed == "Yes" else 0
property_enc = {"Rural":0, "Semiurban":1, "Urban":2}[property_area]

# Predict button
if st.button("Predict Loan Approval"):
    # Prepare feature array
    features = np.array([[gender_enc, married_enc, education_enc, self_employed_enc,
                          dependents, applicant_income, coapplicant_income, loan_amount,
                          loan_amount_term, credit_history, property_enc]])
    
    # Scale numeric features
    scale_cols = [5,6,7,8]  # indices of numeric columns in features
    features[:, scale_cols] = scaler.transform(features[:, scale_cols])
    
    # Make prediction
    prediction = model.predict(features)
    
    # Show result
    if prediction[0] == 1:
        st.success("Loan Approved ")
    else:
        st.error("Loan Not Approved ")
