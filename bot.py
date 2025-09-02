import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import openai

# گرفتن متغیرها از Environment
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ست کردن API
openai.api_key = OPENAI_API_KEY

# استارت بات
async def start(update: Update, context):
    await update.message.reply_text("سلام! من ربات ChatGPT هستم 🤖✌️")

# هندل پیام‌ها
async def handle_message(update: Update, context):
    user_message = update.message.text

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=200
    )

    await update.message.reply_text(response.choices[0].text.strip())

def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()
