import requests

response = requests.get('https://api.covid19api.com/summary')
print(response.status_code)
print(response.text)