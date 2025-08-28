import telebot
import webbrowser
from telebot import types
import sqlite3


bot = telebot.TeleBot('8211500630:AAFopU3hQF4QVqLGpDS-nymsjBed-wRgq8A')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на са=nт')
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Редактировать')
    markup.row(btn1 )
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)

    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'WEbsite is open')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'delete')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://learn.javascript.ru')
    btn2 = types.InlineKeyboardButton('Удалить', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Редактировать',  callback_data='edit')
    markup.row(btn1 )
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Заебись!', reply_markup=markup)

    

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('edit text', callback.message.chat.id, callback.message.message_id )

bot.polling(non_stop=True)

