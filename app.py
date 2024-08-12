import pandasai
from pandasai.llm.local_llm import  LocalLLM
from pandasai.llm.openai import OpenAI
from pandasai.llm.openai import openai
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from dotenv import load_dotenv
import os
import sklearn

def configure():
    load_dotenv()

logo_url = './assets/logo.png'
tokenkey = OpenAI(api_token=os.getenv('api_token'))
modelOpenAI=tokenkey

#ambil api dari streamlit
#tokenkey=st.secrets["api_key"]
#========================

st.sidebar.image(logo_url)
st.title("BitDip A.I tools - for Data Analytics ")
upload_csv = st.file_uploader("upload file yang akan dianalisa dalam bentuk CSV", type=['csv'])

if upload_csv is not None:
    data = pd.read_csv(upload_csv)
    st.write(data.head(3))

#ini di pake untuk test ollama local server    df = SmartDataframe(data, config={"llm": model})
    df = SmartDataframe(data, config={"llm": modelOpenAI})

    prompt = st.text_area("Masukan pertanyaan anda terkait data tersebut.")

    if st.button("Cari Jawaban"):
        if prompt:
            with st.spinner("BitDip Agent melakukan anlisa data dan mencari jawaban untuk anda, mohon sabar cuy..."):
                st.write(df.chat(prompt))
