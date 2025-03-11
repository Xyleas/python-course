import gradio as gr
import openai
import os

# NEVER upload API keys to Github!
#testing openai.api_key = 'SECRETKEY'
openai.api_key = os.environt.get('OPENAI_API_KEY')

messages = []
messages.append({'role': 'system', 'content': 'You are a quiz. Present the user with a multiple-choice question to practice for a python interview, they have to respond by typing a, b, c, d, or e. Wait until the user responds before presenting a new question'})

def respond(history, new_message):
    #testing print(history)

    # Add the user input to the messages
    messages.append({'role': 'user', 'content': new_message})

    # Send the API call
    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages= messages)

    # Obtain response text
    assistant_message = response.choices[0].message
    messages.append()

    return history + [[new_message, assistant_message.content]]

with gr.Blocks() as my_bot:
    chatbot = gr.Chatbot()
    user_input = gr.Text()
    #testing gr.Text(label = "your name")
    #testing gr.TextArea()
    #testing gr.Button()

    user_input.submit(respond, [chatbot, user_input], chatbot)

my_bot.launch()

