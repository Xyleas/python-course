from bs4 import BeautifulSoup
import requests

# Learning basic BeautifulSoup functionality

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify()) # Prints the tree structure of the HTML document.
#print(soup.title, '\n')
#print(soup.title.string)
# print(soup.p.b)
#print(soup.p['class'])
#print(soup.a['href'])

# print(soup.find(href="http://example.com/lacie"))
#print(soup.find(class_ = 'story')) # Underscore for BS because Python has a 'Class' keyword.

# a_tags = print(soup.find_all('a')) # List of all 'a' tags.
# print(a_tags[2]) # Prints the 3rd element
# print(soup.find_all(['a', 'title'])) # Finds all 'a' && 'title' tags

p = soup.find(class_ = 'story')
# print(p.contents)

#for child in p.children: # First layer of descendants.
#    print(child)
body = soup.find('body')
#print(body.contents)
#print(len(body.contents))

#print(list(body.descendants)) # Needs casted
#print(len(list(body.descendants)))

# print(soup.a.parent)
# for p in soup.a.parents: # .parents (GOING UP)
#    print(p.name)

a = soup.a
# print(a.next_sibling.next_sibling)
# print(a.next_sibling.previous_sibling)
# print(a.previous_sibling.previous_sibling)

response = requests.get('https://en.wikipedia.org/wiki/Bristlecone_pine')

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.text)

print('\n', '\n')

# Challenge queries for the Bristlecone pine page.
# 1. Get the text of the top level heading (h1).
# 2. Gind how many second level heading (h2) tags there are. 
# 3. Extract the href of the first link on the page.

# My attempt: print(class_ ="firstHeading mw-first-heading")
# My attempt: print(len(soup.find_all('h2')))
# My attempt: print(soup.find('a')['href'])

print(soup.a['href'])
