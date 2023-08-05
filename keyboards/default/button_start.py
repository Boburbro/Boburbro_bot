from telebot.types import ReplyKeyboardMarkup, KeyboardButton

btns = [
    KeyboardButton('CryLat'),
    KeyboardButton('Pul kiritish'),
    KeyboardButton('Fikr bildirish'),
    
]
btns1 = [
    KeyboardButton('/start')
]
markup1 = ReplyKeyboardMarkup(resize_keyboard=True).add(*btns, row_width=2)
markup1 = markup1.add(*btns1,row_width=2)