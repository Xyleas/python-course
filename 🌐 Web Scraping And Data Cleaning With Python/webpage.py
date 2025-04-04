from bs4 import BeautifulSoup
import requests
import re


def get_html(url, path):
    response = requests.get(url)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(response.text)

# get_html("https://en.wikipedia.org/wiki/Bristlecone_pine", './') # Comment now that it's done.

with open('./html_docs/bristlecone.html', 'r', encode = 'utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
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

# print('Second method: ', infobox.find_all(another_taxonomy_filter))

p_content = soup.find_all(p)
print(p_content)

body_links = []
for p in p_content:
    body_links += p.find_all('a')
#print(body_links)

body_links = list(filter(lambda a: '#cite' not in a['href'], body_links))
#print(body_links)

links = {}
for a in body_links:
    links[a['title']] = 'https://en.wikipedia.org' + a['href']

#print(links)

imgs = soup.find_all('img')
#print(imgs)

for i in imgs:
    if 'class' in i.attrs:
        print(i['class'])
    else:
        print(i)

imgs = list(filter(lambda img: 'class' in imgs.attrs, imgs))
imgs = list(map(lambda img: img['class'][0] == 'mw-file-element', imgs))
print(imgs)

def download_image(url, path):
    response - requests.get(url)
    with open(path, 'wb') as f:
        f.write(response.content)

download_image('https:' + imgs[0]['src'], './image.png')

# Challenge Question
# Create a small dataset of citations from the article in the form of a list.,
# - Examine the citation section in the HTMl tree
# - Extract citations
# - Filter to only citaitons that have an ISBN or DOI
# -  Clean up the data (remove HTML)

try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the references section
        references_header = soup.find('span', {'id': 'References'})
        if not references_header:
            return [] # Return empty list if no reference section is found
        references_list = references_header.find_parent('h2').find_next_sibling('div', class_='reflist')

        citations = []
        if references_list:
            for li in references_list.find_all('li'):
                citation_text = str(li) # Get the entire li tag as a string
                if 'ISBN' in citation_text or 'doi:' in citation_text.lower():
                    # Remove HTML tags using regex
                    cleaned_citation = re.sub(r'<[^>]+>', '', citation_text)
                    # Remove extra whitespace
                    cleaned_citation = ' '.join(cleaned_citation.split())
                    citations.append(cleaned_citation)

        return citations

except requests.exceptions.RequestException as e:
    print(f"Error fetching URL: {e}")
    return []
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    return []


# Solution
citations = soup.find('ol', attrs={'class': 'references'})
cite_tags = citations.find_all('cite')
print(cite_tags[0].text)

isbn_doi = [c.text for c in cite_tags if 'ISBN' in c.text or 'doi' in c.text]
print(isbn_doi)