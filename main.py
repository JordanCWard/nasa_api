import streamlit as st
import requests

# NASA API for APOD: Astronomy Picture of the Day
api_key = "6HaoNM9mBRHnKyYyh3xEnoNwAPqgDFr0dDw1JfvM"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# Get a JSON dictionary with the data
nasa_api = requests.get(url)
data = nasa_api.json()

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns(3)

with col2:
    st.title(data["title"])
    st.image(data["url"])
    st.write(data["explanation"])
