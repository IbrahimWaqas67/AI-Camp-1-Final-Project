import streamlit as st
import joblib
Mirror=joblib.load('Claydoh.pkl')
Certificate=st.slider ("Calories",0,1000,300)
if st.button ("predict"):
  Resullt=Mirror.predict([[Certificate]])
  st.write("AI thinks that this is ",Result[0])
