import requests
from requests.api import request

response = requests.get('http://206.189.44.36:8900/students/')

results = response.json()

for user in results:
    if user['age']>18:
        print('soversh')
    if user['age']<18:
        print('nesoversh')
    print(user['age'], user['name'], user['phone'])