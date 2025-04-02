import telebot

token = ('your_token')  # instead of "your_token", stake your token
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)

bot.infinity_polling()
