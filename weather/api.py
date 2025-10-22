### Load data from a list of cities and put it into a SQLite database file

#import packages
import requests
import os
from dotenv import load_dotenv
import sqlite3
from datetime import datetime

#get API key from the environment file
load_dotenv()
API_KEY = os.getenv('WEATHER_KEY')

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

#List the cities to get data for
cities = ("Brighton", 
          "Wolverhampton", 
          "Hitchin", 
          "Rome", 
          "Nice"
          )

#Create the functions to get the data from the API and save it into the database
def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    return response.json()

def save_weather(city, weather_data):
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            city TEXT,
            temperature REAL,
            feels_like REAL,
            wind_speed REAL,
            humidity REAL,
            description TEXT,
            timezone REAL,
            timestamp TEXT
        )
    """)
    
    cursor.execute("""
        INSERT INTO weather (city, temperature, feels_like, wind_speed, humidity, description, timezone, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        city,
        weather_data["main"]["temp"],
        weather_data["main"]["feels_like"],
        weather_data["wind"]["speed"],
        weather_data["main"]["humidity"],
        weather_data["weather"][0]["description"],
        weather_data["timezone"],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))
    
    conn.commit()
    conn.close()

#run the loop to get and save the data for each city specified
for c in cities:
    data = get_weather(c)
    save_weather(c, data)