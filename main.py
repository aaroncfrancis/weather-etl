from extract import extract_weather_data
from transformers import transform
from load import load_to_demo
from cities import list_of_cities
import pandas as pd

df = pd.DataFrame()

for city in list_of_cities:
    CITY_NAME, COUNTRY_CODE = city[0], city[1]

    # extract
    raw_df = extract_weather_data(CITY_NAME, COUNTRY_CODE)
    if raw_df is not None:

        # transformers
        transformed_df = transform(raw_df)

        df = pd.concat([df, transformed_df])

        # load
        load_to_demo(transformed_df,'weather_data_all_cities', schema="schema1")

print(df)
