#import databutton as db
import streamlit as st
import openai
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

#tokenkey = OpenAI(api_token=os.getenv('api_token'))
#modelOpenAI=tokenkey

modelOpenAI=openai.api_key=os.getenv('api_token')
from utils import get_data


def key_check():
    """
    Checks the OpenAI API key, either from the Databutton secrets store or from user input.
    If the key is valid, it continues the app flow; otherwise, it stops the app and provides feedback.
    """
    try:
        # Attempting to get the OpenAI API key from the Databutton secrets store.
        modelOpenAI#openai.api_key = db.secrets.get(name="OPENAI_API_KEY")

        # Check if the connection is established and models are available.
        if not openai.Model.list():
            st.write("Not connected to OpenAI.")
            st.stop()

    except Exception as e:
        # Display information about needing an OpenAI API key.
        mtinfo = st.empty()
        mtinfo.info(
            """
            Hi there! Welcome to the "One-Prompt Charts" app template. 📊
            
            This app allows you to upload your data and get visual insights with just a single prompt. However, to power the magic behind the scenes, I need your OpenAI API key. 
            
            If you don't have a key, you can sign up and create one [here](https://platform.openai.com/account/api-keys).
            
            Don't worry, your key will be securely stored in the Databutton secrets store, which you can find in the left-side menu under "Configure". If you prefer to add it manually, ensure to assign the name as `OPENAI_API_KEY` for your secret.
            
            Once set up, simply upload your data, prompt about it, and see it visualized! ✨

            """,
            icon="🤖",
        )