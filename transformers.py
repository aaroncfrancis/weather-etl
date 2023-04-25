import pandas as pd
import datetime

# df = extract_weather_data(CITY_NAME=, COUNTRY_CODE=)

def add_temperature_units(df):
    df ['temperature_(c)'] = df ['temperature_(k)'] - 273.15
    df ['temperature_(f)'] = ( df ['temperature_(k)'] - 273.15 ) * 9/5 + 32
    return df

# def transform_humidity_units(df):
#     df ['humidity_(fraction)'] = ( df ['humidity_(%)'] ) / 100
#     return df

def add_timestamp(df):
    date = datetime.datetime.utcnow()
    date_string = date.strftime('%Y-%m-%d %H:%M:00')
    df['utc_time'] = date_string
    return df

def transform(df):
    df = add_temperature_units(df)
    df = add_timestamp(df)
    df = df[['utc_time','city_name','country_code','wind_speed_(m/s)','temperature_(c)','temperature_(f)','weather_description','humidity_(%)']]
    return df 
