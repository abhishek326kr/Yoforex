from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests

# Replace these with your own tokens
TELEGRAM_TOKEN = '7046808243:AAGo73Hr-AtZXbShdXzgk8OkUjYEnsO3g00'
WIT_AI_TOKEN = 'UGH3DOWCFYQOZ55BXETRGGWTL7AEGBSX'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! I am your bot powered by Wit.ai. How can I assist you today?")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    
    # Send the message to Wit.ai
    response = requests.get(
        'https://api.wit.ai/message',
        headers={'Authorization': f'Bearer UGH3DOWCFYQOZ55BXETRGGWTL7AEGBSX'},
        params={'q': user_message}
    )
    data = response.json()

    # Extract intent and entities
    intent = data['intents'][0]['name'] if data['intents'] else 'unknown'
    entities = data['entities']

    reply = f"Detected intent: {intent}\nEntities: {entities}"

    await update.message.reply_text(reply)

def main() -> None:
    application = Application.builder().token("7046808243:AAGo73Hr-AtZXbShdXzgk8OkUjYEnsO3g00").build()


    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
