import http.client
import requests # Must be installed via pip - 'pip install requests'

# Response Example
response = requests.get('https://www.example.com')
print(response.status_code)
print(response.text)

# Http Client Example
conn = http.client.HTTPSConnection("www.example.com")
conn.request("GET", "/")

response = conn.getresponse()
print(response.status, repsonse.reson)

data = response.read()
print(data)

conn.close()