import json
import requests

input_data = {
  "pregnancies": 2,
  "Glucose": 1000,
  "BloodPressure": 120,
  "SkinThickness": 10,
  "Insulin": 100,
  "BMI": 25,
  "DiabetesPedigreeFunction": 0.352,
  "Age": 35
}

url = "http://0.0.0.0:80/diabetes_prediction"

json_object = json.dumps(input_data)

response = requests.post(url, data=json_object).text

# Use json.loads() to convert the string to a dictionary
response_dict = json.loads(response)

# Assuming response_dict is your dictionary
label_value = response_dict['label']

# Now you have the value associated with the 'label' key
print(label_value)