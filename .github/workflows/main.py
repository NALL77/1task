import telebot

bot = telebot.TeleBot('5682663477:AAG5oVYerimx9EfYjCdxFeDekajQ_P4SM_w')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html' )

bot.polling(none_stop=True)
