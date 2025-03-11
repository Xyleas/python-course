import requests

api_endpoint = 'https://localhost:11434/api/generate'

messages = []

while true:
    # Capture user input
    user_input = input("You: ")

    # Updating messages
    messages.append({'role': 'user', 'content': user_input})

    # Send chat to the LLM
    data = {
        'model': 'llama2',
        'stream': False,
        'messages': messages
    }

    response = requests.post(api_endpoint, json=data)

    if response.status_code == 200:
        response_data = response.json()
        assistant_response = response_data['message']['content']

        # Updating messages with response
        messages.append(response_data['message'])
        
        # Showing the repsonse to the user
        print(f'Assistant: {assistant_response}')

    else:
        print('Failed to get response from Ollama API')

   

    