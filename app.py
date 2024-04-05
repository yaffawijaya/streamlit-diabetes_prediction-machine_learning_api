# importing Important Liberaries
import json
import requests
import pickle
import streamlit as st
import numpy as np


# Web Title
st.title('Diabetes Prediction')

# Split Columns
col1, col2 = st.columns(2)

with col1 :
  Pregnancies = st.number_input('Enter the Pregnancies value')

with col2 :
  Glucose = st.number_input('Enter the Glucose value')
  
with col1 :
  BloodPressure = st.number_input('Enter the Blood Pressure value')

with col2 :
  SkinThickness = st.number_input('Enter the Skin Thickness value')

with col1 :
  Insulin = st.number_input('Enter the Insulin value')

with col2 :
  BMI = st.number_input('Enter the BMI value')

with col1 :
  DiabetesPedigreeFunction = st.number_input('Enter the Diabetes Pedigree Function value')

with col2 :
  Age = st.number_input('Enter the Age value')
  
# Input data
input_data = {
  "pregnancies": Pregnancies,
  "Glucose": Glucose,
  "BloodPressure": BloodPressure,
  "SkinThickness": SkinThickness,
  "Insulin": Insulin,
  "BMI": BMI,
  "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
  "Age": Age 
}

## Load model by url
API_MODEL = "http://0.0.0.0:80/diabetes_prediction"
json_object = json.dumps(input_data)
response = requests.post(API_MODEL, data=json_object).text

# Use json.loads() to convert the string to a dictionary
response_dict = json.loads(response)

# Prediction
diabetes_diagnosis = ''

if st.button('Diabetes Prediction Test'):
  if(response_dict.get('label')==1):
    diabetes_diagnosis = 'The patient has diabetes'
  else :
    diabetes_diagnosis = 'The patient does not have diabetes'

st.success(diabetes_diagnosis)

