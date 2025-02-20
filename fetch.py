import os
import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

# Your WeatherAPI key (Replace with your actual key)
API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"

# Cities to fetch weather data for
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]

# List to store data
weather_data = []

# Fetch data for each city
for city in cities:
    params = {
        "key": API_KEY,
        "q": city
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    # Extract relevant information
    weather_data.append({
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "City": data["location"]["name"],
        "Country": data["location"]["country"],
        "Temperature_C": data["current"]["temp_c"],
        "Humidity_%": data["current"]["humidity"],
        "Condition": data["current"]["condition"]["text"]
    })

# Convert to DataFrame
df = pd.DataFrame(weather_data)
print(df.head())
DATABASE_URL = os.getenv("DATABASE_URL")
# Create engine for Neon.tech PostgreSQL
engine = create_engine(DATABASE_URL)

print("✅ Data stored successfully in Neon.tech PostgreSQL!")
