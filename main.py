import telebot

bot = telebot.TeleBot('6693004315:AAHSVg80aziZF4yeI5W-L6V2ZK1a_0z_9nM')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Что вы хотите сделать с этим ботом?', parse_mode='Markdown')


@bot.message_handler(commands=['talk'])
def main(message):
    bot.send_message(message.chat.id, '*Сегодня чудесная погода*', parse_mode='Markdown')


@bot.message_handler(commands=['wiki'])
def main(message):
    bot.send_message(message.chat.id, '[Википедия](https://ru.wikipedia.org/wiki)', parse_mode='Markdown')


bot.infinity_polling()