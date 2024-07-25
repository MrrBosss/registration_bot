import telebot
from telebot.types import Message
from keyboard import get_keyboard, num_send, get_currency
import requests as r
from pprint import pprint 


url ='https://cbu.uz/uz/arkhiv-kursov-valyut/json/'
res = r.get(url)
data = res.json()
bot = telebot.TeleBot("7112484625:AAEcdBbCnu9ZJ7BQ1hSb3Ei5Z6HDltvyOSU")
user_info = {}
#start comandasi uchun ma'sul func
@bot.message_handler(commands=['start'])
def send_wlcome(message:Message):
    chat_id = message.chat.id
    greeting = "Welcome to register bot!"
    bot.send_message(chat_id,greeting,reply_markup=get_keyboard())

#messagelar uchun ma'sul func
@bot.message_handler(func=lambda message:message.text == "Ro'yxatdan o'tish")
def send_text(message:Message):
    chat_id = message.chat.id
    user_info[chat_id] = {}
    msg = bot.send_message(chat_id,'Ismingizni kiriting!')
    bot.register_next_step_handler(msg,take_name)

def take_name(message:Message):
    chat_id = message.chat.id
    user_info[chat_id]['name'] = message.text.title()
    msg = bot.send_message(chat_id,'Raqamingizni kiriting',reply_markup=num_send())
    bot.register_next_step_handler(msg,take_num)


def take_num(message:Message):
    chat_id = message.chat.id
    if chat_id in user_info:
        user_info[chat_id]['number'] = message.contact.phone_number
    bot.send_message(chat_id,f"{user_info[chat_id]['name']}\n{user_info[chat_id]['number']}",reply_markup=get_currency())

@bot.message_handler(func=lambda message:message.text == "Dollar kursini bilish")
def take_currency(message:Message):
    chat_id = message.chat.id
    c,d,r = 'AQSH dollari','Date: 23.04.2024', 'Rate: 12711.00'
    bot.send_message(chat_id,f'Currency: {c}\n {d}\n {r}')

print('bot working')
bot.polling()
