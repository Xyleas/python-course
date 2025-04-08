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

table = data['Australia']
first_row = table.tr
#for td in first_row:
#    print(td.text)

columns = []
for td in first_row:
    if td.text.strip() != '':
        columns.append(td.text.strip())
# print(columns)

rows = table.tbody.find_all('tr')
# print(rows[1])

example_row = row[1]
table_cells = example_row.find_all('td')
print(table_cells)

row_data = {}
for i in range(len(table_cells)):
    row_data[columns[i]] = table_cells[i]

print(row_data['Country'])
print(row_data['Old-growth forest type'])

australia_table = []

def extract_row_data(columns, row):
    row_data = {}

    table_cells = row.find_all('td')

    for i in range(len(table_cells)):
        row_data[columns[i]] = table_cells[i]
    
    return row_data

rows.pop(0)
for r in rows:
    australia_table.append(extract_row_data(columns, row))

# print(australia_table[0])

def clean_row_data(row: dict): # declaring dict helps VSCode w/ completion

    for k in row.keys():
        val = row[k]

        if re.match('\s', val.text):
            row[k] = 'No data'

        links = val.find_all('a')

        for l in links:
            if l.get('title') is not None and '(page does not exist)' in l.get('title'):
                l.replace_with(l.text)

            if 'cite' in l.get('href'):
                l.parent.decompose()

        if k == 'Old-growth extent' and row[k] != 'No data':
            data = row[k].text.strip()

            data = data.replace('\xa0', ' ') # A common unicode space replacer that can cause issues.

            # 2,000  7,800,000
            data = re.search('\d+(?:,\d{3})*(?:\.\d*)? (?:hectares|square kilometres|ha|acres)', data).group()

            parent = row[k].parent
            row[k].decompose()

            new_tag = soup.new_tag('td')
            new_tag.string = data
            parent.append(new_tag)
            
            row[k] = new_tag

    return row

print(clean_row_data(australia_table[2]))

def prepare_table_data(columns, table):
    table_data = []

    rows = tables.find_all('tr')
    rows.pop(0)

    for r in rows: 
        r = extract_row_data(columns, r)
        r = clean_row_data(r)
        table_data.append(r)

    return table_data

def prepare_all_tables(columns, data):
    for k in data.keys():
        data[k] = prepare_table_data(columns, data[k])

    return data

data = prepare_all_tables(columns, data)
#print(len(data), '\n')
#print('FINAL DATA TEST: \n', data['Eurasia'])

#print(data['Australia'][3]['Old-growth extent'].text)

# How many of the lsited forests are in France?

eurasia = data['Eurasia']
france = [r for r in eurasia if 'France' in x['Country'].text]
print(len(france))

australia = data['Australia']
tasmania = [r for r in austalia if 'Tasmania' in r['Area'].text]
priunt(len(tasmania))

tasmania_area_data = [r for r in tasmnaia if r['Old-growth extent'] != 'No data']

total = 0
for r in tasmania_area_data:
    area = r['Old-growth extent'].text
    
    area = area.replace(',', '')
    val = re.search('\d*', area).group()
    val = float(val)

    if 'square kilometres' in are:
        val = val * 100

    total += val

print('Total area for Tasmania forests: ', total, ' ha')

bulgaria_rows = []
for row in data['Eurasia']:
    if row['Country'].text.strip() == 'Bulgaria':
        bulgaria_rows.append(row)

bulgaria_link = 'https://wikipedia.org' + bulgaria_rows[0]['Country'].a['href']

# get_html(bulgaria_link, './bulgaria.html') # Comment out line when done.

with open('./html_docs/bulgaria.html', 'r', encoding='utf-8') as f:
    bulgaria_html = f.read()

soup = BeautifulSoup(bulgaria_html, 'html.parser')

print(bulgaria_soup.title)

def get_bulgaria_are(tag):
    return tag.name == 'td' and 'km' in tag.text and 'Total' in tag.parent.text

km_tags = [t.text for t in bulgaria_soup.find_all(get_bulgaria_area)]
area_tag = km_tags[0] 

print(area_tag)

b_area = re.search('\d+(?:,\d{3})*(?:\.\d*)?', area_tag).group()
b_area = float(b_area.replace(',',''))

print(b_area)

b_area = b_area * 100

forest_total = 0
for row in bulgaria_rows:
    forest_data = row['Old-growth extent'].text
    forest_data = re.search('\d+(?:,\d{3})*(?:\.\d*)?', forst_data).group()
    forest_data = forest_data.replace(',','')
    forest_data = float(forest_data)

    forest_total += forest_total

print(forest_total)

print('Percentage of Bulgarian land area accounted for by old growth: ', round(forst_total/ b_area) * 100, 5, '%')

# Challenge analytics:
#
# How many different U.S. states have forests with some
# variety of oak tree?

us_table = data['United States']
states = set()
for r in us_table:
    f_type = r['Old-growth forest type']
    if f_type is not None and f_type != 'No data':
        if 'oak' in f_type.text.lower():
            states.add(r['Country'].text.strip())

print(states)
print(len(states))

