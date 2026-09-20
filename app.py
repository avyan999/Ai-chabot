"""
Gemini AI Agent - Streamlit version
Run with: streamlit run app.py
"""

import os
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="Agent", page_icon="🤖")

if not api_key:
    st.error("GEMINI_API_KEY not found. Add it to your .env file as GEMINI_API_KEY=your_key_here")
    st.stop()

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.5-flash-lite"
SYSTEM_INSTRUCTION = "You are a helpful, friendly assistant. Keep replies clear and concise."


# ---- Tools: this is what turns a plain chatbot into an "agent" ----
# The model decides on its own whether it needs to call these.

def get_current_time() -> str:
    """Get the current date and time."""
    return datetime.now().strftime("%A, %d %B %Y, %I:%M %p")


def calculate(expression: str) -> str:
    """Evaluate a basic math expression, e.g. '12 * 7 + 3'.

    Args:
        expression: A math expression using only numbers and + - * / ( ).
    """
    allowed = set("0123456789+-*/(). ")
    if not all(ch in allowed for ch in expression):
        return "Invalid expression - only numbers and + - * / ( ) are allowed."
    try:
        return str(eval(expression))  # noqa: S307 - input is character-restricted above
    except Exception as e:
        return f"Could not calculate: {e}"


# Create the chat session once per browser session - Streamlit reruns this whole
# script on every interaction, so anything that must survive a rerun goes in
# st.session_state.
if "chat_session" not in st.session_state:
    st.session_state.chat_session = client.chats.create(
        model=MODEL,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            tools=[get_current_time, calculate],
        ),
    )
    st.session_state.messages = []

st.title("🤖 Agent")
st.caption("Can check the time and do quick math on its own when it needs to.")

# Redraw past messages every rerun
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle a new message
if prompt := st.chat_input("Ask something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.chat_session.send_message(prompt)
                reply = response.text
            except Exception as e:
                reply = f"Error: {e}"
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})