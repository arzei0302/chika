import telebot


bot = telebot.TeleBot('6459750758:AAFmjgRCn4ach9QVIXFCDMIoLZunfQrfAf8')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!')
    

bot.polling(none_stop=True)