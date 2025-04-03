from bs4 import BeautifulSoup
import requests
import re

response = requests.get("https://en.wikipedia.org/wiki/Bristlecone_pine")
print(response.text)

def get_html(url, path):
    response = requests.get(url)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(response.text)

# get_html("https://en.wikipedia.org/wiki/Bristlecone_pine", './') # Comment now that it's done.

with open('./html_docs/bristlecone.html', 'r', encode = 'utf-8') as f:
    html = f.read()

soup - BeautifulSOup(html, 'html.parser')
# print(soup.title)

#section_headings = soup .find_all('span', attrs={'class': 'mw=headline'})
#print(section_headings)

section_headings = [span.string for span in section_headings] # Funciton within a list?!? It works, and is unique to Python
# section_headings = [span.text for span in section_headings] # Not a BS4 object.
#print(section_headings)
#print(type(section_headings[0]))
#print(section_headings[0].parent)

taxonomy = {}

infobox = soup.find('table', attrs={'class': 'infobox biota'})
print(infobox)

def taxonomy_filter(tag):
    return ':' in tag.text and tag.name == 'td'

filtered = infobox.find_all(taxonomy_filter)
print(filtered)

for tag in filtered:
    sibling = tag.next_sibling.next_sibling
    # print(sibling)

    taxonomy[tag.text.strip().replace(':', '')] = sibling.text.strip()

print(taxonomy)

def another_taxonomy_filter(tag):
    return tag.name == 'tr' and len(list(tag.children)) == 4

print('Second method: ', infobox.find_all(another_taxonomy_filter))