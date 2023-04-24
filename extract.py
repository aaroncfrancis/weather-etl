import requests 
import datetime as dt

BASE_URL = "http://api.openweathermap.org/data/2.5/wewather?"
API_KEY = open('api_key', 'r').read()
CITY = "London"

url = BASE_URL + "appid=" + "API_KEY" + "&q=" + CITY

response = requests.get(url).json()

print(response)