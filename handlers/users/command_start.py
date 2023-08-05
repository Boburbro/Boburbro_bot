from loader import bot 
from telebot.types import Message, ReplyKeyboardRemove
from functions.function import isAdmin, isNewMember, addNewMember
from keyboards.default.button_start import markup1
from states.state1 import STATE1_
from states.state2 import STATE2_
from telebot.util import extract_arguments

@bot.message_handler(commands=['start'])
async def command_start(message: Message):
    await bot.delete_state(message.from_user.id,message.chat.id)
    

    if isNewMember(message.chat.id):
        if addNewMember(message.chat.id):
            await bot.send_message(chat_id=message.chat.id, text=f'Assalomu alaykum! {message.from_user.full_name}\nSiz botimizda yangisiz!', reply_markup=markup1)
        else:
            await bot.send_message(chat_id=message.chat.id, text='/start')
    else:
        await bot.send_message(chat_id=message.chat.id, text=f'Assalomu alaykum! {message.from_user.full_name}\nSiz botimizda eskisiz!', reply_markup=markup1)
    text = extract_arguments(message.text)
    if text == 'fikr':
        await bot.send_message(chat_id=message.chat.id, text='Fikringizni qoldiring', reply_markup=ReplyKeyboardRemove())
        await bot.set_state(message.from_user.id, STATE2_.State1, message.chat.id)
    elif text == 'CryLat':
        matn="""
Marxamat matn kiriting men uni Kril bo'lsa Lotinga Lotin bo'lsa Krilga aylantirib beraman! 
Bo'limdan chiqish uchun /start ni bosing.
"""
        await bot.send_message(chat_id=message.chat.id, text=matn, reply_markup=ReplyKeyboardRemove())
        await bot.set_state(user_id=message.from_user.id, state=STATE1_.State1)
    elif text == 'Pulkiritish':
        text='Karta raqam:\n\n8600052938509880\nYM'
        await bot.send_message(message.chat.id, text)

            
        
