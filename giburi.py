from flask import Flask
import requests, json
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'testdb'
app.config["MONGO_URI"] = "mongodb://localhost:27017/testdb"
mongo = PyMongo(app)


## Get JSON
response = requests.get('https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49')
print(response.status_code)
json_data = response.text
title = json.loads(json_data)['title']

## Save Data
collection = mongo.db["titles"]
collection.insert_one({"title": title})
print("saved data.")
