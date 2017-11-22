import requests


response = requests.get('http://localhost:5002/employees')

if response.status_code != 200:
    print ('Something went wrong')

print (response.json())
