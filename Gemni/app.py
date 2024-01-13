# In this app we are creating a simple text generating app using gemni_pro api

from dotenv import load_dotenv
load_dotenv() 
import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load gemini pro model
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


# STREAMLIT APP
st.set_page_config(page_title="GEMINI PRO API FOR TEXT GENERATION")
st.header("GEMINI LLM APP")
input = st.text_input("Input: ", key="input")
submit = st.button("Generate Content")
if submit:
    response = get_gemini_response(input)
    st.write(response)