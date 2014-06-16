import requests

body = {'Name': 'Eric', 'Age': '26'}

response = requests.post("http://codecademy.com/learn-http/",data=body)
print response
