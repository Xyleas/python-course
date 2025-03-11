import requests
import base64

# Load image
with open('sample_image.jpg', 'rb') as image_file:

    # 1. Read it's contents (binary).
    image_data = image_file.read()

    # 2. Turn binary into Base64.
    base64_image_data = base64.b64encode(image_data)

    # 3. Encode into UTF-8
    base64_image_string = base64_image_data.decode('utf-8')

api_endpoint = 'https://localhost:11434/api/generate'

data = {
    'model': 'llava',
    'stream': False,
    'prompt': 'Describe the image provided: ',
    'images': [base64_image_string]
}

response = requests.post(api_endpoint, json=data)

if response.status_code == 200:
    response_data = response.json()
    print(response_data['response'])

else:
    print('Failed to get response from Ollama API')