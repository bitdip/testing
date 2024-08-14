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

#ambil api dari streamlit
#api_dari_streamlit =st.secrets["api_token"]
#tokenkey = OpenAI(api_token=api_dari_streamlit)
#========================

modelOpenAI=tokenkey
st.sidebar.image(logo_url)
st.image(logo_url,width=150)
st.title("BitDip A.I tools - for Data Analytics ")

#upload_csv = get_data()
#else:
#    df = st.chat_message("TIDAK ADA FILE DI UPLOAD")
# If data is uploaded successfully
#if upload_csv is not None:
#upload_csv=get_data()
upload_csv = st.file_uploader("upload file yang akan dianalisa dalam bentuk CSV", type=['csv'])

if upload_csv is not None:
    data = pd.read_csv(upload_csv)
    st.write(data.head(3))

#ini di pake untuk test ollama local server    df = SmartDataframe(data, config={"llm": model})
    df = SmartDataframe(data, config={"llm": modelOpenAI})

    prompt = st.text_area("Masukan pertanyaan anda terkait data tersebut.")
    respon =""
    if st.button("Cari Jawaban"):
        if prompt:
            with st.spinner("BitDip Agent melakukan anlisa data dan mencari jawaban untuk anda, mohon sabar cuy..."):
#                result=st.write(df.chat(prompt))
#                respon=st.write(df.chat(prompt))
#                generatedcode = df.last_code_generated
#                print(generatedcode)
                result = df.chat(prompt)
#                respon=result
                if isinstance(result, str):
                    respon=result
#                    print("ini respon if 1 ",  respon)
#                    posisi = result.find(".png")
#                    print(posisi)
                    if ".png" in respon:
                        print("ADA PNG")
                        st.image(respon)
                    else:
                        print(respon)
                     #   st.text(respon)
                        st.write(respon)
                        print("ini if instace")
                else:
                    #print(result)
                    st.write(result)
                    print("ini if root")
#                elif isinstance(result, int):
#                    st.text(respon)


             #   print =st.write(df.chat(prompt))
               # df.chat(prompt)
               # if.df
                #print(st.info(response))
                #Image._show(a)
#                try:

                    #st.image(st.write(df.chat(prompt)))
                    #st.image(df.chat(prompt))
 #               except Exception:
 #                   pass
