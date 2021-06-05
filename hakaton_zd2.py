import requests
import json

new_student = {
    "name": "oggi",
    "age": 19,
    "group": "Python-3",
    "phone": "+996704551306",
    "email": "oggi20@gmail.com",
    "created_by": "team_4"
}

response = requests.post('http://206.189.44.36:8900/students/', data = new_student)

result = response.json()
print(result)
print(result[id])

response = requests.get('http://206.189.44.36:8900/students/10/')
res = response.json()
res2 =(res["name"], res["age"], res["group"])
print(res2)