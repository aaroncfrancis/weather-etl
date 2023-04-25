from extract import extract_weather_data
from transformers import add_temperature_units
from load import load_to_demo

CITY_NAME = input('Input City Name: ')
COUNTRY_CODE = input('Input Country Code: ')

# extract
raw_df = extract_weather_data(CITY_NAME, COUNTRY_CODE)

# transformers
transformed_df = add_temperature_units(raw_df)

print(transformed_df)

# # load
# load_to_demo(transformed_df,'weathertable', schema="schema1")


list_of_cities = [1,1]