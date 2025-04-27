import requests
from telegram import Update
from telegram.ext import Application, MessageHandler, CallbackContext, filters

# Your Ngrok public URL for the Flask server
FLASK_SERVER_URL = 'Replace with your Ngrok URL'  

# Function to send the input text to the Flask server and get the prediction
def ask_ollama(message):
    response = requests.post(
        f'{FLASK_SERVER_URL}/predict',  # The Flask server endpoint
        data={'input_text': message},
        timeout=60  # Timeout after 1 minute
    )

    if response.status_code == 200:
        result = response.json()['result']

        # Remove <think> tags if present
        result = result.replace("<think>", "").replace("</think>", "").strip()

        # Fix Markdown formatting for Telegram (converting "**" and "##" to bold and headers)
        result = result.replace("**", "*").replace("##", "➤ ")

        return result
    else:
        return "❌ Error contacting the syed's local server. Deployment in progress.... Please try again later."

# Handler for incoming messages
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text

    # Send "Thinking..." message while processing
    thinking_message = await update.message.reply_text("🤖 Thinking...")

    bot_reply = ask_ollama(user_message)

    # Edit the "Thinking..." message with the actual response
    await thinking_message.edit_text(bot_reply)

# Main function to start the bot
def main():
    TELEGRAM_TOKEN = 'Your Telegram Bot token'  

    # Initialize the application (bot)
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Register the message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
