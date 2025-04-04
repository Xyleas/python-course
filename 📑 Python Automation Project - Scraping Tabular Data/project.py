from bs4 import BeautifulSoup
import requests
import re

def get_html(url, path):
    response = requests.get(url)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(response.text)

# get_html("https://en.wikipedia.org/wiki/List_of_old-growth_forests", './') # Comment now that it's done.

with open('./html_docs/bristlecone.html', 'r', encode = 'utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table', attrs={'class': 'wikitable sortable'}) # jquery-tablesorter'}) # jquery dynamically changed the class
print(len(tables))
print(tables[0])

data = {}

for t in tables:
    heading = t.find_previous_sibling(['h2', 'h3']).text.replace('[edit]', '')
    data[heading] = t

# print('\n', data['Australia'])

