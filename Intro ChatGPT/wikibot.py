import openai
import wikipedia

# Pass the API key
openai.api_key = 'SecretKey'

# Get user input
title = input('title of the page: ')

# Get the Wikipedia content
page = wikipedia.page(title = title, auto_suggest = False)

# Define the prompt
#testing prompt = 'Create a 5-bullet point summary of:' + page.content[:10000]
prompt = 'Write a summary of the following article:' + page.content[:10000]
messages[]
message = {'role': 'user', 'content': prompt}
#testing message.append(message)

try: 
    # Make an API call
    response = openai.ChatCompletion.create(model = 'gpt-3.5-turgo', messages = messages)

    # Print the response
    print(response.choices[0].message.content)
    print(response.choices[1].message.content)

# Authentication issue
except openai.error.AuthenticationError:
    print('no valid token / authentication error')

except openai.error.InvalidRequestError as e:
    print('invalid request, read the manual!')
    print(e)