# LLM Deployment on a Local PC (Local Flask API + Telegram Bot)

---

## 📜 Overview

This project demonstrates how to deploy a **Locally Running LLM (Ollama + Deepseek-R1 model)** on your personal computer, exposing it through a **Flask API**, and interacting with it via a **Telegram Bot**.

It allows you to run a fully private AI chatbot locally — without sending your data to cloud services.  
Perfect for those who want **privacy**, **speed**, and **full control** over their AI chatbot!

You can interact with the local LLM by simply messaging a Telegram Bot, which forwards your queries to your PC via Ngrok.

---


## 🛠 Requirements

- Python 3.9+
- Ollama installed and running locally
- Ngrok for exposing local Flask API
- Telegram Bot Token (from BotFather)

---

## 📦 Installation

1. Clone the Repository
```bash
git clone https://github.com/your-username/ollama-local-telegram-bot.git
cd ollama-local-telegram-bot
```

2. Create a Virtual Environment (optional but Recommended)

It is recommended to use a virtual environment to manage project dependencies separately.
   
```py
python -m venv venv
```
On Linux/Mac

```py
source venv/bin/activate 
```
On Windows

```py
venv\Scripts\activate    
```

3. Install Dependencies
   
```py
pip install -r requirements.txt
```

---

## ⚙️ Setup

### 1. Start Ollama Server

Make sure Ollama is installed and the Deepseek-R1 model is available locally:

```py
ollama run deepseek-r1
```

### 2. Run Flask Server

```py
python flask_server.py
```

- This starts a Flask server at http://localhost:8000
- It listens for POST requests with user input text and forwards it to Ollama.

### 3. Start Ngrok

Expose your local Flask server:

```py
ngrok http 8000
```

Copy the public URL provided by Ngrok (e.g., https://abcd1234.ngrok.io).

### 4. Configure Telegram Bot

- Replace the following placeholders inside telegram_bot.py:
  - FLASK_SERVER_URL with your Ngrok public URL
  - TELEGRAM_TOKEN with your Bot Token from BotFather

Example:

```bash
FLASK_SERVER_URL = 'https://abcd1234.ngrok.io'
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
```

---

## 🤖 Running the Telegram Bot

```py
   python telegram_bot.py
```

The bot will now listen to incoming messages, forward them to your local AI model, and send back the responses!

---

## 💬 How It Works

- User sends a message to Telegram Bot.
- Telegram Bot sends the message to Flask server via Ngrok tunnel.
- Flask server uses subprocess to pipe the message to ollama run deepseek-r1.
- Ollama processes the input and returns the AI-generated response.
- Flask sends the response back to the Telegram Bot.
- Bot edits the original "Thinking..." message to show the final reply.

Everything happens locally on your machine, ensuring privacy and control! 🔒

---

## 📄 Files Explained

| File | Description |
|:----|:------------|
| flask_server.py | Runs the local Flask API that interacts with the Ollama model. |
| telegram_bot.py | Telegram bot code to send/receive messages and interact with Flask API. |
| requirements.txt | List of Python libraries needed. |
| README.md | Project documentation and setup guide. |

---

## 📢 Important Notes

- Keep Ngrok session active; otherwise, the bot will not reach your local server.
- Ngrok free version provides a temporary URL which changes every session unless you have a paid plan (custom domain).
- Ollama and model files must be preinstalled locally before running the server.

---

## ✨ Future Improvements

- Add authentication to Flask API.
- Automatic Ngrok URL updater inside Telegram Bot.
- Deploy using Reverse Proxy (like Nginx) for production setups.
- Add multiple model support based on user choice.

---

# 🚀 That's it!

You are now running a fully private LLM-powered chatbot on your local machine, accessible globally through Telegram!

---

## 👨‍💻 Developer Info

Made with ❤️ by `salmanfareeth`

---

## ⚠️ Disclaimer

This project is developed purely for educational and personal learning purposes.  
The developer does not guarantee the performance, security, or production-readiness of this project.

Usage of this project is at your own risk.  
Please ensure you understand the dependencies and third-party tools (such as Ollama, Flask, Ngrok, and Telegram) involved.  

The developer is not responsible for any misuse or damage caused by deploying or modifying this project.

---
