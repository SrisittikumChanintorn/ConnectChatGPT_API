import os
from openai import OpenAI
from openai_chatbot import Normal_LLM



# Initialize the OpenAI API client
instruction = "คุณเป็น AI assistant ที่เป็นมิตรและช่วยเหลือ"
model_name = "gpt-3.5-turbo-16k"
api_key = 'YOUR_API_KEY'  # Replace with your actual OpenAI API key


# Initialize the OpenAI API client
llm1 = OpenAI(api_key=api_key)


# Start the chat loop
chat_history = []
query = None  # Initialize query to avoid potential reference error

while True:
    if not query:
        query = input("User: ")
    if query in ['quit', 'q', 'exit']:
        break
    result = Normal_LLM(query, llm1, chat_history,model_name=model_name, instruction=instruction)
    print("Chatbot:", result)

    chat_history.append((query, result))
    query = None