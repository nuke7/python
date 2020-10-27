import requests

url = 'https://my-json-server.typicode.com/typicode/demo/comments'


x = requests.get(url)

print(x.json())

my_object = x.json()

for o in my_object:
    print(o["id"])
