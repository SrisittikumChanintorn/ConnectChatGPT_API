# ChatGPT Terminal App

This simple application lets you chat with OpenAI's ChatGPT directly from your computer terminal.

## What is this program ?

Talk to ChatGPT without using a web browser! Just type your questions or messages, and the AI will respond right in your terminal window.

The program can:
- Connect to OpenAI's GPT model
- Remember your conversation history
- Follow custom instructions you set

## Getting started

1. Make sure you have Python installed
2. Install the required package: `pip install openai==1.68.2` by folliwong this step

   ```bash
      pip install -r requirements.txt
   ```
   
3. Add your OpenAI API key in the `main.py` file where it says "YOUR_API_KEY"
4. Run the program in CMD : `python main.py`

## How to use

After starting the program:
1. Type your question after "User: "
2. Read the AI's response
3. Continue the conversation
4. Type "quit", "q", or "exit" when you want to stop

## Customizing the AI

You can change how the AI responds by editing the "instruction" line in `main.py`. The current instruction is in Thai and tells the AI to be friendly and helpful.

## Files included

- `main.py` - The main program
- `openai_chatbot.py` - Handles communication with OpenAI
- `requirements.txt` - Lists required software

Enjoy chatting with AI from your terminal!
