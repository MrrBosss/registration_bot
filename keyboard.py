from telebot.types import KeyboardButton,ReplyKeyboardMarkup

def get_keyboard():
    board = ReplyKeyboardMarkup(resize_keyboard=True)
    board.add(KeyboardButton("Ro'yxatdan o'tish"))
    return board

def num_send():
    but = ReplyKeyboardMarkup(resize_keyboard=True)
    but.add(KeyboardButton("Raqam jo'natish" ,request_contact=True))
    return but

def get_currency():
    currency = ReplyKeyboardMarkup(resize_keyboard=True)
    currency.add(KeyboardButton("Dollar kursini bilish"))
    return currency
