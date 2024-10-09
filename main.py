import streamlit as st
import requests

st.set_page_config(layout="wide")

content = """
    kjhcjxzcjkxzvjksjckvnjkcxvlkcxjlkvc xclvjclkxvj cxkl vjlkcxjv 
    """

st.write(content)

st.header("Our Team")

# NASA API for APOD: Astronomy Picture of the Day
api_key = "nYoltU1gTNUfsd3WBB5cqQEV6mLdkUm7DW906hEr"
url = "https://api.nasa.gov/planetary/apod"

# Get a JSON dictionary with the data
website = requests.get(url)
content = website.json()
