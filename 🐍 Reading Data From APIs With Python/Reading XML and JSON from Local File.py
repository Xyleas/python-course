from urllib.request import urlopen
import json
from bs4 import BeautifulSoup as soup

json_filename = 'Storm Tide JSON.json'
f = open(json_filename)
json_data = json.load(f)
print(json_data)
print(json_data['help'])

xml_filename = ''
f = open(xml_filename)
xml_data = soup(f, 'xml')
print(xml_data)
