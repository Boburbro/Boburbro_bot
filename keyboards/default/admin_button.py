from telebot.types import ReplyKeyboardMarkup, KeyboardButton

btns = [
    KeyboardButton('Bazani olish'),
    KeyboardButton('Statitika'),
    KeyboardButton('Chiqish'),
    
]
admin_markup1 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(*btns)