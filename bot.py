# Вместо your_token поставьте свой токен // instead of your_token, stake your token

import telebot  # импортируем telebot // importing telebot

token = ('your_token')  # сохраняем токен бота // save the bot token
bot = telebot.TeleBot(token)  # создаем бота // сreating a bot

@bot.message_handler(content_types=['text']) # хэндлер, который срабатывает на текст // handler that triggers on text
def echo(message): # объявляем функцию "echo" // announcing the "echo" function
    bot.send_message(message.chat.id, message.text)  # повторяем сообщение юзера // repeating the user's message

bot.infinity_polling() # long polling