import streamlit as st
import pandas as pd
import joblib
model =joblib.load("KNN.pkl")
scaler=joblib.load("scaler.pkl")
expected_columns=joblib.load("columns.pkl")

st.title("Heart stroke prediction ")
st.markdown("provide the following detials")

# detials about you original dataframe 
Age	=st.slider("AGE",18,100,40)
Sex=st.selectbox("SEX", ["M","F"])
ChestPainType=st.selectbox("chest pain type",["ATA",'NAP','TA','ASY'])

Age = st.slider("Age", 18, 100, 40)
Sex = st.selectbox("Sex", ["M", "F"])
ChestPainType = st.selectbox("Chest pain type", ["ATA", "NAP", "TA", "ASY"])
RestingBP = st.number_input("Resting blood pressure (mm Hg)", 80, 200, 120)
Cholesterol = st.number_input("Cholesterol (mg/dl)", 100, 600, 200)
FastingBS = st.selectbox("Fasting blood sugar > 120 mg/dl", [0, 1])
RestingECG = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
MaxHR = st.slider("Max heart rate", 60, 220, 150)
ExerciseAngina = st.selectbox("Exercise-induced angina", ["Y", "N"])
Oldpeak = st.slider("Oldpeak (ST depression)", 0.0, 6.0, 1.0)
ST_Slope = st.selectbox("ST slope", ["Up", "Flat", "Down"])
 

if st.button('Predict'):
    rawdata={
         "Age": Age,
        "RestingBP": RestingBP,
        "Cholesterol": Cholesterol,
        "FastingBS": FastingBS,
        "MaxHR": MaxHR,
        "Oldpeak": Oldpeak,
        "Sex_" + Sex: 1,
        "ChestPainType_" + ChestPainType: 1,
        "RestingECG_" + RestingECG: 1,
        "ExerciseAngina_" + ExerciseAngina: 1,
        "ST_Slope_" + ST_Slope: 1,
        }
    input_df=pd.DataFrame([rawdata])
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col]=0
    
    input_df=input_df[expected_columns]
    
    scaled=scaler.transform(input_df)
    prediction= model.predict(scaled)[0]
    if prediction == 1:
        st.error( "🚨 HIGH RISK OF HEART ATTACK\n\n" "⚠️ Your results indicate a potentially elevated risk. " "Please consult a qualified healthcare professional for proper evaluation." )
    else: st.success( "💚 LOW RISK OF HEART ATTACK\n\n" "✅ Your results indicate a lower predicted risk. " "This does not guarantee that you are free from heart disease." )

