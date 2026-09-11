# Simple Gemini Chatbot 🤖

A simple command-line AI chatbot built with Python and Google's Gemini API.

The chatbot maintains conversation history during the current session, allowing it to remember previous messages in the conversation.

## Features

* 💬 Interactive command-line chatbot
* 🧠 Maintains conversation history during the session
* ⚡ Uses Google's Gemini API
* 🔐 API key stored securely in a `.env` file
* 🛑 Type `exit` or `quit` to stop the chatbot
* 📝 Simple and beginner-friendly Python code

## Requirements

* Python 3.9+
* A Gemini API key
* Internet connection

## Project Structure

```text
simple-gemini-chatbot/
│
├── chatbot.py
├── .env
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install google-genai python-dotenv
```

## API Key Setup

Create a `.env` file in the project folder:

```env
GEMINI_API_KEY=your_api_key_here
```

**Important:** Never upload your `.env` file or API key to GitHub.

Make sure `.env` is included in `.gitignore`.

## Run the Chatbot

Run:

```bash
python chatbot.py
```

You should see:

```text
Chatbot ready. Type 'exit' or 'quit' to stop.

You:
```

Now type your message:

```text
You: Hello

Bot: Hello! How can I help you today?
```

The chatbot remembers messages from the current conversation.

To stop it:

```text
You: exit

Bot: Goodbye!
```

## How It Works

The program:

1. Loads the Gemini API key from `.env`.
2. Creates a Gemini API client.
3. Creates a chat session.
4. Sends user messages to Gemini.
5. Prints the AI response.
6. Continues the conversation until the user enters `exit` or `quit`.

## Model

The project currently uses:

```python
MODEL = "gemini-3.5-flash-lite"
```

You can change the model in `chatbot.py` if you have access to another Gemini model.

## Security

Do **not** hard-code your API key inside `chatbot.py`.

Bad:

```python
api_key = "AIza..."
```

Good:

```python
api_key = os.getenv("GEMINI_API_KEY")
```

Keep your `.env` file private.

## Future Improvements

Possible improvements:

* Add streaming responses
* Add a graphical user interface
* Add conversation export
* Add persistent chat history
* Add configurable system instructions
* Add support for multiple AI models
* Add better error handling

## License

This project is for learning and educational purposes.
