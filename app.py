
import streamlit as st
import joblib

model = joblib.load('salary_predictor.pkl')

st.title('Salary Predictor')
years = st.slider('Years of Experience', 0.0, 30.0, 5.0)

if st.button('Predict'):
    prediction = model.predict([[years]])[0]
    st.success(f'Predicted Salary: ${prediction:,.2f}')
    st.info(f'Expected Range: ${prediction-7059:,.2f} - ${prediction+7059:,.2f}')
