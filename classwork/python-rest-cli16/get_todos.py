import sys
import requests
import json

user_input = sys.argv[1]


#print(user_input)

r = requests.get('https://jsonplaceholder.typicode.com/todos/'+ user_input)

json_data = r.json()

print(json_data)

