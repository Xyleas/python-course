import requests

api_endpoint = 'https://jsonplaceholder.typicode.com/posts/1'
updated_data = {
    'id': '1',
    'title': 'Updated Title',
    'body': 'updated BODY',
    'userId': 1
}

response = requests.delete(api_endpoint)

if response.status_code == 201:
    print("Data deleted successfully")
    # print(response.json())
else:
    print(f"Failed to deleted data.")