import requests 
import pandas as pd
import datetime as dt
from creds import API_KEY

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def extract_weather_data(CITY_NAME: str, COUNTRY_CODE: str) -> pd.DataFrame:  #type hinting
    url = f"{BASE_URL}?q={CITY_NAME},{COUNTRY_CODE}&appid={API_KEY}"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:

        # Parse response as JSON
        data = response.json()

        # Extract relevant weather information
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Print weather information
        print(f"Weather description: {weather_description}")
        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")
        print(f"Wind speed: {wind_speed} m/s")

        # Convert data to pandas dataframe
        weather_data = pd.DataFrame({
            'Weather Description': [weather_description],
            'Temperature (K)': [temperature],
            'Humidity (%)': [humidity],
            'Wind Speed (m/s)': [wind_speed]
        })

        return weather_data

    else:
        print("Failed to fetch weather data.")