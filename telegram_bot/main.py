import telebot
import webbrowser
from telebot import types


link = 'https://nsk.rossko.ru/'
BOT_TOKEN = '6801756421:AAF88hmyPjQMXiWUHt8F-wwF9By3t2R8r3Y'
bot = telebot.TeleBot(token=BOT_TOKEN)


@bot.message_handler(commands=['site', 'website'])
def open_site(message):
    webbrowser.open(link)


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')


@bot.message_handler()
def answers(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    elif message.text.lower() == 'i need my info':
        bot.send_message(message.chat.id, message)
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID {message.from_user.id}')


@bot.message_handler(content_types=['photo', 'file'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    site_button = types.InlineKeyboardButton('Go to website', url=link)
    delete_button = types.InlineKeyboardButton('Delete photo', callback_data='delete')
    edit_button = types.InlineKeyboardButton('Edit text', callback_data='edit')
    markup.row(site_button, delete_button)
    markup.row(edit_button)
    bot.reply_to(message, 'Очень красивое фото', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


bot.polling(non_stop=True)
