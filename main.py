import telebot


bot = telebot.TeleBot('6351868903:AAFG1H_LZSF9sdGhUIMkNkp9ndJZrtmgIZ4')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Hello')

bot.polling(none_stop=True)
