"""
    STEPS:

    1. Code must run top-down
    2. Comment out / delete all code that only shows output / view
    3. Get our code out of Jupyter
    4. CLEAN UP
    5. Wrap code into functions
    6. Add arguments to our functions (i.e. what flexibility does the user have?)
"""

import requests
import pandas as pd

SECRET_KEY = 'a2b30bd526c3b5962010ec6b3f0dd7bc'
LATITUDE = '38.8935124'
LONGITUDE = '-77.1550059'
TIMESTAMP = '1483246800'

def get_weather_df(key, lat, lon, ts, step=5, interval='86400'):

    """
    Given an API Key, a Latitude, a Longitude, a Timestamp,
    a TimeStep (default of 5), and an interval (optional)...

    Return a DataFrame with this information.

    All arguments / inputs must be strings, except step (int).
    """

    timestamps = []
    for i in range(step):
        t = int(ts) + i*int(interval)
        timestamps.append(str(t))

    dfs = []
    for t in timestamps:
        url = f'https://api.darksky.net/forecast/{key}/{lat},{lon},{ts}'
        result = requests.get(url)
        result_json = result.json()
        final_result = pd.DataFrame(result_json['hourly']['data'])
        dfs.append(final_result)

    all_weather = pd.concat(dfs, sort=True)
    all_weather.set_index('time', inplace=True)

    return all_weather

df = get_weather_df(SECRET_KEY, LATITUDE, LONGITUDE, TIMESTAMP)
