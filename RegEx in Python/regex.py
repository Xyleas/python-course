import re

data = 'Welcome to this Welcome course on Regualr Expressions! Today\'s date is the 28th of August.'

# print(re.search('Welcome', data).group())
# print(re.findall('Welcome', data))
# print(re.findall('e', data))

# Metacharacters
# . * + ?

# .
# print(re.findall('t.', data))

# * 
# print(re.findall('t*o', data))
# print(re.findall('s*i', data))

# +
# print(re.findall('t+o', data))

# ?
# print(re.findall('s?i', data))

# print(re.findall('\.',data))

# Character Classes

# [abc]
# print(re.findall('[abc]', data))
# [0-9]
# print(re.findall('[0-9]', data))
# print(re.findall('[A-Za-z]', data)) # Must be in ASCII Order (Smaller -> Larger)
#

# \d \w \s
# print(re.findall('\d',data)) # Digits
# print(re.findall('\w',data)) # Words
# print(re.findall('\s',data)) # (White) Spaces

# print(re.findall('\d+\w+\s',data))

# Anchors
# ^ (Beginning) $ (End)

# print(re.findall('^\w*', data))
# print(re.findall('^\w*.$', data))

# print(re.findall('^.*!', data))

# Quantifiers
# {n} {n,} {n,m}

# print(re.findall('\w{3}', data))
# print(re.findall('\w{3,}', data))
# print(re.findall('\w{2,3}', data))

# print(re.findall('\w{1,}', data))
# print(re.findall('\w+', data))

# Groups
# () (?:)

# print(re.search('(\d+)(th)', data).groups())

#print(re.search('(?:\w+ \w+)', data).group())
#print(re.search('(?:\w+ \w+){3}', data).group())

#print(re.findall('(?: \w{7} | \w{4})', data))

# Challenge Question

# Use groups to capture arbitrary phone numbers.
# Including optional country code.

# Must cover the following inputs:
# (999)999-9999
# +13(999)999-9999

# Do not assume that any one section has a certain number if digits
# For instance, this could be matched also:
# +124(99999)99-999-99999999-9

#data0 = '(999)999-9999'
#data1 = '+13(999)999-9999'
#data2 = '+124(99999)99-999-99999999-9'

#data = [data0, data1, data2]

#for i in data:
#    print(re.findall('(?:\+\d+)?\(\d+\)(?:\d+-)+\d+', data)) # Country Code: (?:\+\d+)? , 

content = "The Rocky Mountains, also known as the Rockies, are a major mountain range and the largest mountain system in North America. The Rocky Mountains stretch 3,000 miles (4,800 kilometers)[3] in straight-line distance from the northernmost part of Western Canada, to New Mexico in the Southwestern United States. Depending on differing definitions between Canada and the U.S., its northern terminus is located either in northern British Columbia's Terminal Range south of the Liard River and east of the Trench, or in the northeastern foothills of the Brooks Range/British Mountains that face the Beaufort Sea coasts between the Canning River and the Firth River across the Alaska-Yukon border.[4] Its southernmost point is near the Albuquerque area adjacent to the Rio Grande rift and north of the Sandia–Manzano Mountain Range. Being the easternmost portion of the North American Cordillera, the Rockies are distinct from the tectonically younger Cascade Range and Sierra Nevada, which both lie farther to its west."

sentences = re.split('(?<![A-Z])\.(?!\d)', content) # ?< look back, ? look ahead

for s in sentences:
    print('TOKEN: ', s.strip(), '\n')
print()

final_data = []
for s in sentences:
    if re.search('\d', s):
        final_data.append(s.strip())
        print("DATA: ", s.strip(), '\n')