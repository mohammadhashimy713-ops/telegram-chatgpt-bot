import telebot

# توکن رباتی که از BotFather گرفتی رو اینجا بذار
TOKEN = "اینجا_توکن_ربات_تو_بذار"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "سلام ✨ من چت جی پی تی نیستم، اما ربات تستی هستم!")

print("ربات روشن شد...")
bot.infinity_polling()
