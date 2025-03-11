import openai

# Pass the API key
openai.api_key = 'SecretKey'

# Define the prompt
messages[]
message = {'role': 'system', 'content': 'you are a CTO mentoring developers, dont only provide answers also ask guiding questions'}
message = {'role': 'user', 'content': 'why is my website down?'}
#testing message.append(message)

try: 
    # Make an API call
    response = openai.ChatCompletion.create(model = 'gpt-3.5-turgo', messages = messages, temperature = 0, n = 2, max_tokens = 200, )

    # Print the response
    print(response.choices[0].message.content)
    print(response.choices[1].message.content)

# Authentication issue
except openai.error.AuthenticationError:
    print('no valid token / authentication error')

except openai.error.InvalidRequestErroras e:
    print('invalid request, read the manual!')
    print(e)