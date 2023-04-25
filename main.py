from extract import extract_weather_data
from transformers import add_temperature_units
from load import load_to_demo

# extract
raw_df = extract_weather_data('Montreal', 'CA')

# transformers
transformed_df = add_temperature_units(raw_df)

# load
load_to_demo(transformed_df,'weathertable', schema="schema1")


