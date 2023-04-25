import requests 
import pandas as pd
import datetime as dt
from creds import API_KEY

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def extract_weather_data(CITY_NAME: str, COUNTRY_CODE: str) -> pd.DataFrame:  #type hinting
    url = f"{BASE_URL}?q={CITY_NAME},{COUNTRY_CODE}&appid={API_KEY}"
    
    try: 
        # Check if the request was successful
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if HTTP error occurs
        data = response.json()

        # Extract relevant weather information
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # # Print weather information
        # print(f"Weather description: {weather_description}")
        # print(f"Temperature: {temperature} K")
        # print(f"Humidity: {humidity}%")
        # print(f"Wind speed: {wind_speed} m/s")

        # Convert data to pandas dataframe
        weather_data = pd.DataFrame({
            'city_name': [CITY_NAME],
            'country_code': [COUNTRY_CODE],
            'weather_description': [weather_description],
            'temperature_(k)': [temperature],
            'humidity_(%)': [humidity],
            'wind_speed_(m/s)': [wind_speed]
        })

        return weather_data
    
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {CITY_NAME}", err)
        return None
