import telebot


bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Hello')

bot.polling(none_stop=True)
