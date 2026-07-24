from ollama import ChatResponse, chat

response: ChatResponse = chat(model='mistral:7b', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content']) # print the response

