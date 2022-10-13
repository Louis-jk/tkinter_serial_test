import requests
import json

# URL = 'https://dongnaebook.app'
URL = 'https://jsonplaceholder.typicode.com/posts'
res = requests.get(URL).text
res_info = json.loads(res)

print(res)
