import pandasai 
from pandasai.llm.local_llm import LocalLLM
from pandasai.llm.openai import OpenAI
from pandasai.llm.openai import openai
from pandasai.responses.response_parser import ResponseParser
from pandasai.responses.response_type import ResponseType
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from dotenv import load_dotenv
import os
import sklearn
from PIL import Image
import io
import string
import re

def configure():
    load_dotenv()

logo_url = './assets/logo.png'
tokenkey = OpenAI(api_token=os.getenv('api_token'))


modelOpenAI=tokenkey
st.sidebar.image(logo_url)
st.image(logo_url,width=150)
st.title("BitDip A.I tools - for Data Analytics ")

#upload_csv = st.file_uploader("upload file yang akan dianalisa dalam bentuk CSV", type=['csv'])

file_type =["csv", "xlsx", "xls"]
upload_csv = st.file_uploader("Upload a data file", type=file_type)

if upload_csv:
    if upload_csv.name.endswith('.csv'):
        data = pd.read_csv(upload_csv)
    elif upload_csv.name.endswith('.xlsx') or upload_csv.name.endswith('.xls'):
        data = pd.read_excel(upload_csv)
    else:
        data = None

if upload_csv is not None:
    with st.expander("Show data"):
        st.write(data)

    df = SmartDataframe(data, config={"llm": modelOpenAI})

    prompt = st.text_area("Masukan pertanyaan anda terkait data tersebut.")
    respon =""
    if st.button("Cari Jawaban"):
        if prompt:
            with st.spinner("BitDip Agent melakukan anlisa data dan mencari jawaban untuk anda, mohon sabar cuy..."):
                result = df.chat(prompt)
                if isinstance(result, str):
                    respon=result
                    if ".png" in respon:
                        st.image(respon)
                    else:
                        print(respon)
                        st.write(respon)
                else:
                    st.write(result)
