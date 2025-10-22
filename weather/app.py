#import packages

import streamlit as st
import requests
import os
from dotenv import load_dotenv
#import sqlite3
#from datetime import datetime

# Get API key from the environment file
load_dotenv()
API_KEY = os.getenv('WEATHER_KEY')

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Create the functions to get the data from the API and save it into the database
def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    return response.json()

# Create the app
st.title("🌍 Global Weather Dashboard")

city = st.text_input("Enter city name:", "London")
if st.button("Get Weather"):
    data = get_weather(city)
    #save_weather(city, data)
    st.write(f"**{city}** - {data['main']['temp']}°C, {data['weather'][0]['description']}")