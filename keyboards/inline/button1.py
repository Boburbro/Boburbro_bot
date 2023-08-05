from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

btsn = [
    InlineKeyboardButton(text="⭐️⭐️⭐️⭐️⭐️", callback_data='5'),
    InlineKeyboardButton(text="⭐️⭐️⭐️⭐️", callback_data='4'),
    InlineKeyboardButton(text="⭐️⭐️⭐️", callback_data='3'),
    InlineKeyboardButton(text="⭐️⭐️", callback_data='2'),
    InlineKeyboardButton(text="⭐️", callback_data='1'),
    
    
    
    
]

InlineMatkup1 = InlineKeyboardMarkup(row_width=1).add(*btsn)