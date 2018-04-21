import requests

a = requests.get('http://192.168.0.194/', {'a': 3})
print(1, a)
b = requests.post('http://192.168.0.194/', {'a': 3})
print(1, b)

