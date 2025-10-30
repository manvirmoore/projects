### Load data from a list of cities and put it into a SQLite database file

# import packages
import requests
import os
from dotenv import load_dotenv
import sqlite3
from datetime import datetime

# get API key from the environment file
load_dotenv()
API_KEY = os.getenv('WEATHER_KEY')

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

# List the cities to get data for - places I've been in the last few years
cities = ("Brighton", 
          "Wolverhampton",
          "Rome",
          "Copenhagen",
          "Dublin",
          "Athens",
          "Amsterdam",
          "Monaco",
          "Los Angeles", 
          "Barcelona"
          )

# Number of timestamps
ts = 8

# Create the functions to get the data from the API and save it into the database
def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric", "cnt":ts}
    response = requests.get(BASE_URL, params=params)
    return response.json()

def save_weather(city, weather_data):
    conn = sqlite3.connect("weather/forecast.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS forecast (
            forecast_time TEXT,
            city TEXT,
            temperature REAL,
            feels_like REAL,
            wind_speed REAL,
            humidity REAL,
            description TEXT,
            timestamp TEXT
        )
    """)
    for i in range(ts):
        cursor.execute("""
            INSERT INTO forecast (forecast_time, city, temperature, feels_like, wind_speed, humidity, description, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            weather_data["list"][i]["dt_txt"],
            city,
            weather_data["list"][i]["main"]["temp"],
            weather_data["list"][i]["main"]["feels_like"],
            weather_data["list"][i]["wind"]["speed"],
            weather_data["list"][i]["main"]["humidity"],
            weather_data["list"][i]["weather"][0]["description"],
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

    conn.commit()
    conn.close()

# run the loop to get and save the data for each city specified
for c in cities:
    data = get_weather(c)
    save_weather(c, data)