# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 12:26:03 2023

@author: Lenovo
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
heart_model = pickle.load(open('heart_model.sav','rb'))

# sidebar navigatin
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                              ['Diabetes Prediction','Heart Disease Prediction'],
                              icons = ['capsule-pill','clipboard2-pulse'],
                              default_index = 0)
    
# diabetes prediction page 
if (selected == 'Diabetes Prediction'):
    # page title
    st.title('Diabetes Prediction')
    
    #gitting the inpute data from the user
    # input`s columns
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age of the patient')
    
    # code for prediction
    diab_diagnosis = ''
    
    # button for prediction
    if st.button('Diabetes Test Result'):
        diab_pred = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if (diab_pred[0]==1):
            diab_diagnosis = 'The Person is Diabetic'
        else:
            diab_diagnosis = 'The Person is not Diabetic'
            
    st.success(diab_diagnosis)
   
        
    
    
# heart disease prediction page 
if (selected == 'Heart Disease Prediction'):
    # page title
    st.title('Heart Disease Prediction')
    
    #gitting the inpute data from the user
    # input`s columns
    col1,col2,col3 = st.columns(3)
    with col1:
        age = st.text_input('Age of the patient')
    with col2:
        sex = st.text_input('Gender')
    with col3:
        cp = st.text_input('Chest Pain Type')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the Peak exercise ST segment')
    with col3:
        ca = st.text_input('Number of Major vessels')
    with col1:
        thal = st.text_input('Names and Social Security Numbers of the Patients')
    
    # code for prediction
    heart_diagnosis = ''
    
    # button for prediction
    if st.button('Heart Disease Test Result'):
        heart_pred = heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if (heart_pred[0]==1):
            heart_diagnosis = 'The Person has Heart Disease'
        else:
            heart_diagnosis = 'The Person has not Heart Disease'
            
    st.success(heart_diagnosis)
    