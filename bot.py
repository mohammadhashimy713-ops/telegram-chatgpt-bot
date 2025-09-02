import telebot

# توکن رباتی که از BotFather گرفتی
TOKEN = "8262707302:AAELSqDX5MAz6-DWMKd08ARHCD2j8n0RJ40"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "سلام 👋 من ربات تستی هستم، پیام‌تو گرفتم ✅")

print("ربات روشن شد...")
bot.infinity_polling()
