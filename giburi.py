import requests
import json

response = requests.get('https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49')
print(response.status_code)
json_data = response.text
title = json.loads(json_data)['title']
print(title)