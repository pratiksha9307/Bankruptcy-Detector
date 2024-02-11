# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 16:18:17 2023

@author: Admin
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image

pickle_in = open("SVM_P_classifier.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome ALL"
def predict_bankruptcy(industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk):
     prediction=classifier.predict([[industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk]])
     print(prediction)
     return prediction





def main():
   
    html_temp = """
    <div style="background-color:green;padding:10px">
    <h2 style="color:white;text-align:center;"> Bankruptcy Detector </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    industrial_risk = st.text_input("Industrial Risk","Type Here")
    management_risk = st.text_input("Management Risk","Type Here")
    financial_flexibility = st.text_input("Financial Flexibility","Type Here")
    credibility = st.text_input("Credibility","Type Here")
    competitiveness = st.text_input("Competitiveness","Type Here")
    operating_risk = st.text_input("Operating Risk","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_bankruptcy(industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()

