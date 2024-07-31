import streamlit as st 

import pickle

trained_model = pickle.load(open('trained_model.sav','rb'))

 
# Title
st.title("Heart Attack Precdictor")
age = st.text_input("Enter Your age", "0")
gender = st.selectbox("Gender: ",
                     ['Male', 'Female'])
chestpain = st.selectbox("Chest pain type:",["0 = Typical Angina","1 = Atypical Angina","2 = Non-anginal Pain","3 = Asymptomatic"])
trestbps = st.text_input("Enter your Resting blood pressure (in mm Hg)","0")
chol = st.text_input("Enter your  Cholestoral in mg/dl fetched via BMI sensor","0")
fbs = st.selectbox("fasting blood sugar:",['1 = True','0 = False'])
restecg = st.selectbox("Ecg Result:",['0 = Normal','1 = ST-T wave normality','2 = Left ventricular hypertrophy'])
thalach =st.text_input("Maximum heart rate achieved","0")
oldpeak = st.text_input("Old peak value calculated from ecg")
slope = st.text_input("slope value calculated from ecg")
thall = st.selectbox("Thalium Stress Test result:",['0','1','2','3'])
exng = st.selectbox("Exercise induced angina:",['1 = Yes','0 = No'])
caa = st.selectbox("number of major vessels:",['0','1','2','3'])


if st.button('Heart Disease Test Result'):

    user_input = [age,trestbps,chol,thalach, oldpeak, slope,caa, thall,thalach, oldpeak, slope,caa, thall]

    user_input = [float(x) for x in user_input]

    heart_prediction = trained_model.predict([user_input])

    if heart_prediction[0] == 1:
        heart_diagnosis = 'The person is having heart disease'
    else:
        heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
