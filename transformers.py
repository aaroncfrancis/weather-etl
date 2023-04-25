import pandas as pd

# df = extract_weather_data(CITY_NAME=, COUNTRY_CODE=)

def add_temperature_units(df):
    df ['Temperature (C)'] = df ['Temperature (K)'] - 273.15
    df ['Temperature (F)'] = ( df ['Temperature (K)'] - 273.15 ) * 9/5 + 32
    return df

def transform_humidity_units(df):
    df ['Humidity (Fraction)'] = ( df ['Humidity (%)'] ) / 100
    return df


# Calling the methods

