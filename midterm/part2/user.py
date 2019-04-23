import requests
import json

r = requests.get('https://reqres.in/api/users/')

json_data = r.json()

#print of the second item's first & last name, aka = Janet Weaver
print(json_data["data"][1]['first_name'], json_data["data"][1]['last_name'])
