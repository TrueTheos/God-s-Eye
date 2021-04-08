# import requests
# from requests.auth import HTTPBasicAuth
# import pandas as pd
# from pandas.io.json import json_normalize
# import matplotlib.pyplot as plt
# import geoplotlib as gp
# import json
# import ast


# #If you are copy pasting proxy ips, put in the list below
# #proxies = ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']

# wigle_username = 'AID94fefcc92c6b6d72c0ddef51648be624'
# wigle_password = 'c89af7b58bac2ea7da91eded50a7451d'

# payload = {'latrange1':'52.579700454596455', 'latrange2':'52.498490042829104', 'longrange1':'18.414369811023505', 'longrange2':'18.582448558461245', 'api_key': (wigle_username + wigle_password).encode()}

# pune_results = requests.get(url='https://api.wigle.net/api/v2/network/search', params=payload, auth=HTTPBasicAuth(wigle_username, wigle_password)).json()

# print(json.dumps(pune_results, indent=4, sort_keys=True))

# df = json_normalize(pune_results['results'])
# # RENAMING COLUMNS FOR GEOPLOTLIB:
# df = df.rename(columns={'trilat': 'lat', 'trilong': 'lon'})
# cols = list(df.columns)
# # PREVIEWING AVAILABLE INFORMATION:
# print(f"Result obtained has {df.shape[0]} rows and {df.shape[1]} columns in it. \n\nThe list of columns include {cols}")
# print(df)
