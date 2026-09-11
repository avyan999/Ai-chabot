"""
Simple Gemini Chatbot (CLI version)
Keeps conversation history so the bot remembers earlier messages in the same session.
"""

import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load GEMINI_API_KEY from the .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: GEMINI_API_KEY not found.")
    print("Create a .env file in this folder with this line:")
    print("GEMINI_API_KEY=your_key_here")
    sys.exit(1)

client = genai.Client(api_key=api_key)

# Change this to any Gemini model you have access to.
# gemini-3.5-flash-lite is fast, cheap, and covered by the free tier.
MODEL = "gemini-3.5-flash-lite"

SYSTEM_INSTRUCTION = "You are a helpful, friendly assistant. Keep replies clear and concise."


def chat():
    # client.chats.create() tracks conversation history for you automatically
    chat_session = client.chats.create(
        model=MODEL,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION
        ),
    )

    print("Chatbot ready. Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ("exit", "quit"):
            print("Bot: Goodbye!")
            break
        if not user_input:
            continue

        try:
            response = chat_session.send_message(user_input)
            print(f"Bot: {response.text}\n")

        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    chat()
