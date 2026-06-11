import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('churn_model.pkl', 'rb'))

st.title("Customer Churn Prediction")

st.write("Enter customer details below:")

gender = st.selectbox("Gender", [0, 1])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", [0, 1])
Dependents = st.selectbox("Dependents", [0, 1])
tenure = st.number_input("Tenure", min_value=0, max_value=100, value=12)
PhoneService = st.selectbox("Phone Service", [0, 1])
MultipleLines = st.selectbox("Multiple Lines", [0, 1, 2])
InternetService = st.selectbox("Internet Service", [0, 1, 2])
OnlineSecurity = st.selectbox("Online Security", [0, 1, 2])
OnlineBackup = st.selectbox("Online Backup", [0, 1, 2])
DeviceProtection = st.selectbox("Device Protection", [0, 1, 2])
TechSupport = st.selectbox("Tech Support", [0, 1, 2])
StreamingTV = st.selectbox("Streaming TV", [0, 1, 2])
StreamingMovies = st.selectbox("Streaming Movies", [0, 1, 2])
Contract = st.selectbox("Contract", [0, 1, 2])
PaperlessBilling = st.selectbox("Paperless Billing", [0, 1])
PaymentMethod = st.selectbox("Payment Method", [0, 1, 2, 3])
MonthlyCharges = st.number_input("Monthly Charges", value=50.0)
TotalCharges = st.number_input("Total Charges", value=1000.0)

if st.button("Predict Churn"):

    data = np.array([[
        gender,
        SeniorCitizen,
        Partner,
        Dependents,
        tenure,
        PhoneService,
        MultipleLines,
        InternetService,
        OnlineSecurity,
        OnlineBackup,
        DeviceProtection,
        TechSupport,
        StreamingTV,
        StreamingMovies,
        Contract,
        PaperlessBilling,
        PaymentMethod,
        MonthlyCharges,
        TotalCharges
    ]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Customer is likely to Churn")
    else:
        st.success("Customer is likely to Stay")