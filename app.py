import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('model.pkl', 'rb'))
st.title("Heart Disease Prediction App")


age = st.number_input("Age", min_value=0, max_value=120, value=30)
gender = st.selectbox("Gender", ["Male", "Female"])
cholesterol = st.number_input("Cholesterol", min_value=0, max_value=600, value=150)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=300, value=120)
heart_rate = st.number_input("Heart Rate", min_value=0, max_value=220, value=70)
smoking = st.selectbox("Smoking", ["Current", "Never", "Former"])
alcohol_intake = st.selectbox("Alcohol Intake", ["Heavy", "Moderate"])
exercise_hours = st.number_input("Exercise Hours per Week", min_value=0, max_value=168, value=3)
family_history = st.selectbox("Family History of Heart Disease", ["Yes", "No"])
diabetes = st.selectbox("Diabetes", ["Yes", "No"])
obesity = st.selectbox("Obesity", ["Yes", "No"])
stress_level = st.number_input("Stress Level", min_value=0, max_value=10, value=3)
blood_sugar = st.number_input("Blood Sugar", min_value=0, max_value=300, value=100)
exercise_induced_angina = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
chest_pain_type = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])

if st.button("Predict"):
    input_data = pd.DataFrame({
        "Age": [age],
        'Gender': [gender],
        'Cholesterol':[cholesterol],
        'Blood Pressure':[blood_pressure],
        'Heart Rate':[heart_rate],
        'Smoking':[smoking],
        'Alcohol Intake':[alcohol_intake],
        'Exercise Hours':[exercise_hours],
        'Family History':[family_history],
        'Diabetes':[diabetes],
        'Obesity':[obesity],
        'Stress Level':[stress_level],
        'Blood Sugar':[blood_sugar],
        'Exercise Induced Angina':[exercise_induced_angina],
        'Chest Pain Type':[chest_pain_type]
    })
    

    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.write("The model predicts a high risk of heart disease.")
    else:
        st.write("The model predicts a low risk of heart disease.")
