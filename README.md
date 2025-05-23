# LLM Deployment on a Local PC (Local Flask API + Telegram Bot)

---

## 📜 Overview

This project demonstrates how to deploy a **Locally Running LLM (Ollama + Deepseek-R1 model)** on your personal computer, exposing it through a **Flask API**, and interacting with it via a **Telegram Bot**.

It allows you to run a fully private AI chatbot locally — without sending your data to cloud services.  
Perfect for those who want **privacy**, **speed**, and **full control** over their AI chatbot!

You can interact with the local LLM by simply messaging a Telegram Bot, which forwards your queries to your PC via Ngrok.

---

## 🤖 What is Ollama?

Ollama is a framework that allows you to run, manage, and interact with Large Language Models (LLMs) directly on your local machine.  
It provides an easy way to download, start, and communicate with AI models without needing powerful cloud infrastructure.

Ollama supports multiple models and enables private, local, and secure AI experiences.

Official site: https://ollama.com/

---

## 🚀 Why Use Ollama?

- No cloud dependency — run AI models **completely offline** on your PC.
- **More privacy** — your data stays local and secure.
- **Flexibility** — easily switch between different models like DeepSeek, Llama, Qwen, Gemma, phi3 etc.
- **Speed** — faster response times compared to cloud APIs (no network latency).
- **Freedom** — no API costs or rate limits when using your own hardware.

Ollama simplifies local LLM deployment for developers, researchers, and enthusiasts.

---

## 🧠 Why DeepSeek R1?

In this project, I have used the `deepseek-r1` model with Ollama.

Here’s why:

- **Balanced Performance**: DeepSeek R1 offers a great balance between response quality, reasoning ability, and speed.
- **Optimized for Local Use**: It is lighter and faster compared to larger LLMs like Llama 3 or GPT-4, making it ideal for running on a local PC without needing heavy GPU resources.
- **Good General Knowledge**: DeepSeek R1 has strong knowledge across multiple domains, making it very capable for chatbot interactions, Q&A, summarization, and simple coding tasks.
- **Resource Friendly**: It consumes fewer resources (RAM, CPU) which ensures smooth deployment alongside services like Flask and Telegram bots on normal systems.
- **Free and Open**: DeepSeek models are freely available, allowing experimentation and usage without licensing issues.

> In short, DeepSeek R1 was selected to create a **responsive, efficient, and practical AI chatbot experience** that works well even on mid-specification PCs.

Official reference: https://deepseek.com/

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
git clone https://github.com/salmanfareeth/LLM-Deployment.git
cd LLM-Deployment
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
venv\scripts\activate    
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


### 3. 🌐 Setting up Ngrok for Public URL Access

1. **Install Ngrok**:
   - Ngrok is used to expose your local server (Flask in this case) to the internet with a public URL.
   - **Installation steps**:
     - Visit [Ngrok's official website](https://ngrok.com/download) to download the correct version for your operating system.
     - Extract the downloaded file and place it in a directory of your choice.
     - Run the following command in your terminal to verify Ngrok installation:

       ```bash
       ./ngrok --version
       ```

2. **Expose Local Server Using Ngrok**:
   - Once Ngrok is installed, you can expose your Flask server to the web:
     - Run the following command to start a secure tunnel to your local Flask app (on port 8000 in this example):

       ```bash
       ./ngrok http 8000
       ```

     - Ngrok will provide a public URL (like `https://abcd1234.ngrok.io`), which can be used to access your Flask API from anywhere, including for integration with your Telegram bot.

   > **Important**: This Ngrok URL can be used temporarily and should be updated every time the tunnel is restarted (e.g., after system restart).




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

## 🤖 Creating a Telegram Bot using BotFather

1. Open the Telegram app and search for "BotFather".

2. Start a chat with BotFather by clicking "Start".

3. Type `/newbot` and send it.

4. BotFather will ask for a name:
   - This is your bot’s display name (e.g., "Ollama AI Bot").

5. Then it will ask for a username:
   - It must end with 'bot' (e.g., `ollama_deepseek_bot`).

6. After completing, BotFather will send you a **Bot Token**:
   - It looks like: `1234567890:ABCDEF1234GhIjKlmNoPQrstUvWxYZ`
   - **Copy this token** — you will need it for your Python code.

7. Done! 🚀 Your Telegram Bot is now created!

## ⚡ Important:
- Save your Bot Token securely — do not share it publicly.
- To chat with your bot, just search for its username inside Telegram and start messaging.

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

## 🖼️ Demo Screenshot

Here’s a live demo of the Telegram Bot working with Ollama on local PC:

![Telegram Bot Chat Demo](https://github.com/salmanfareeth/LLM-Deployment/blob/main/images/demo_telegram.jpg)

> Screenshot: Chatting with the locally deployed AI bot via Telegram.

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

