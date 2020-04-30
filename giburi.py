import requests
import json
from pymongo import MongoClient
import pandas as pd

response = requests.get('https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49')
print(response.status_code)
json_data = response.text
title = json.loads(json_data)['title']
print(title)

#Takeshi's code
client = MongoClient('localhost', 27017)
db = client['Ghibli'] 
table = db['Ghibli_Titles']
table.insert_many(title)
