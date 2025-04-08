import json
from urllub.request import urlopen

url = 'https://www.data.qld.gov.au/api/3/action/datastore_search?resource_id=7afe7233-fae0-4024-bc98-3a72f05675bd&limit=5'
url_result = urlopen(url)
raw_data = url_result.read()
json_data = json.loads(raw_data)
json_string = json.dumps(json_data)

print (json_string)

result = (json_data['result'])
print(result)

records = result['records']
print(records)

first_record = records[0]
site = first_record['Site']
dateTime = first_record['DateTime']
waterLevel = first_record['Water Level']
prediction = first_record['Prediction']
residual = first_record['Residual']

records_data = []
for record in records:
    record_data = [
        record['Site'],
        record['DateTime'],
        record['Water Level'],
        record['Prediction'],
        record['Residual']
    ]
    records_data.append(record_data)
print(records_data)