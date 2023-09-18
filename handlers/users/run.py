from loader import bot
from telebot.types import Message, ReplyKeyboardRemove
from states.state1 import STATE1_
from states.state2 import STATE2_
from functions.function import isAdmin, getSta
from keyboards.default.button_start import markup1

@bot.message_handler(content_types=['text'])
async def command_help(message: Message):
    if message.text == 'CryLat':
        text="""
Marxamat matn kiriting men uni Kril bo'lsa Lotinga Lotin bo'lsa Krilga aylantirib beraman! 
Bo'limdan chiqish uchun /start ni bosing.
"""

        await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=ReplyKeyboardRemove())
        await bot.set_state(user_id=message.from_user.id, state=STATE1_.State1)
    elif message.text == 'Pul kiritish':
        text='Karta raqam:\n\n8600052938509880\nYM'
        await bot.send_message(message.chat.id, text)
    elif message.text == 'Fikr bildirish':
        await bot.send_message(chat_id=message.chat.id, text='Fikringizni qoldiring', reply_markup=ReplyKeyboardRemove())
        await bot.set_state(message.from_user.id, STATE2_.State1, message.chat.id)
    elif message.text == "Host":
        await bot.send_message(message.chat.id, "Hosting bo'limi tez kunda ishga tushadi va bu bo'limda siz bot yaratishingiz mumkin")

    if message.text == 'Bazani olish' and isAdmin(message.chat.id):
        document = open('baza.db', 'rb')
        await bot.send_document(message.chat.id, document)
    elif message.text == 'Chiqish' and isAdmin(message.chat.id):
        await bot.send_message(chat_id=message.chat.id, text='Bosh menu', reply_markup=markup1 ) 
    elif message.text == 'Statitika' and isAdmin(message.chat.id):
        await bot.send_message(chat_id=message.chat.id, text=f'{getSta()}') 
