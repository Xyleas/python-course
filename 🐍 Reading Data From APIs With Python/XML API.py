from bs4 import BeautifulSoup as BeautifulSoup
from urllib.request import urlopen

url = 'https://apps.des.qld.gov.au/air-quality/xml/feed.php?category=1&region=ALL'
url_result = urlopen(url)
raw_data = url_result.read()
xml_soup = soup(raw_data, 'xml')
print(xml_soup)

southEastQueensland = xml_soup.findAll('region', {'name': 'South East Queensland'})
southEastQueensland = southEastQueensland[0]
print(southEastQueensland)

stations = southEastQueensland.findAll('station')
print(stations)
first_station = stations[0]
print(first_station)

print(sd = first_station.findAll('measurement', {'name':'Sulfer Dioxide'}))

headers = 'Station Name, Nitrogen Dioxide, Ozone, Sulfer Dioxide, Carbon Monoxide, Particle PM10, Particle PM2.5, Particle TSP, Visibility\n'

filename = 'Air Quality XML.csv'
f = open(filename, 'w')

f.write(headers)

for station in stations:
    station_string = ''
    station_name =  station['name']
    nd = station.findAll('measurment', {'name':'Nitrogen Dioxide'})
    nd = '' if len(nd) == 0 else str(nd[0].text) + ','
    o = station.findAll('measurment', {'name':'Ozone'})
    o = '' if len(o) == 0 else str(o[0].text) + ','
    sd = station.findAll('measurment', {'name':'Sulfer Dioxide'})
    sd = '' if len(sd) == 0 else str(sd[0].text) + ','
    cm = station.findAll('measurment', {'name':'Carbon Monoxide'})
    cm = '' if len(cm) == 0 else str(cm[0].text) + ','
    ppm10 = station.findAll('measurment', {'name':'Particle PM10'})
    ppm10 = '' if len(ppm10) == 0 else str(ppm10[0].text) + ','
    ppm2 = station.findAll('measurment', {'name':'Particle PM2.5'})
    ppm2 = '' if len(ppm2) == 0 else str(ppm2[0].text) + ','
    ptsp = station.findAll('measurment', {'name':'Particle TSP'})
    ptsp = '' if len(ptsp) == 0 else str(ptsp[0].text) + ','
    v = station.findAll('measurment', {'name':'Visibility'})
    v = '\n' if len(v) == 0 else str(v[0].text) + '\n'

    station_string += station_name + nd + o + sd + cm + ppm10 + ppm2 + ptsp + v
    f.write(station_string)

