import requests
import pandas as pd
import os
from datetime import datetime
from sqlalchemy import create_engine

# Read API key and database URL from environment variables
API_KEY = os.getenv("WEATHER_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

BASE_URL = "http://api.weatherapi.com/v1/current.json"
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]

# Create engine for Neon.tech PostgreSQL
engine = create_engine(DATABASE_URL)

# Fetch Weather Data
weather_data = []
for city in cities:
    params = {"key": API_KEY, "q": city}
    response = requests.get(BASE_URL, params=params)
    data = response.json()  # Convert response to dictionary

    # Print the API response for debugging
    print(f"Response for {city}: {data}")  

    # Check if the response contains 'location' and 'current' keys
    if "location" in data and "current" in data:
        weather_data.append({
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "City": data["location"]["name"],
            "Country": data["location"]["country"],
            "Temperature_C": data["current"]["temp_c"],
            "Humidity_%": data["current"]["humidity"],
            "Condition": data["current"]["condition"]["text"]
        })
    else:
        print(f"⚠️ Error fetching data for {city}: {data.get('error', 'Unknown error')}")

# Convert to DataFrame and Store in Neon.tech PostgreSQL
if weather_data:
    df = pd.DataFrame(weather_data)
    df.to_sql("weather", con=engine, if_exists="append", index=False)
    print("✅ Data stored successfully in Neon.tech PostgreSQL!")
else:
    print("❌ No data to store.")
