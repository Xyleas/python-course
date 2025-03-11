import openai

# NEVER upload API keys to Github!
openai.api_key = 'SECRETKEY'

messages = []
messages.append({'role': 'system', 'content': 'You are a quiz. Present the user with a multiple-choice question to practice for a python interview, they have to respond by typing a, b, c, d, or e. Wait until the user responds before presenting a new question'})

while True:
    # Send the API call
    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages= messages)

    # Display response in console
    print(response.choices[0].message)

    # Capture user input
    user_input = input('Enter your answer: ')

    # Quit loop if user presses "q"
    if user_input == 'q':
        exit()

    # Prompt preparation
    messages.append({'role': 'user', 'content': user_input})

    # Expanding the conversation
    messages.append(response.choices[0].message)
     
    #testing print(messages)