from loader import bot 
from telebot.types import Message
from functions.function import isAdmin, isNewMemeber, addNewMember

@bot.message_handler(commands=['start'])
async def command_start(message: Message):
    if isAdmin(message.chat.id):
        await bot.send_message(chat_id=message.chat.id, text=f'Assalomu alaykum! Admin')
    else:
        if isNewMemeber(message.chat.id):
            if addNewMember(message.chat.id):
                await bot.send_message(chat_id=message.chat.id, text=f'Assalomu alaykum! {message.from_user.full_name}\nSiz botimizda yangisiz!')
            else:
                await bot.send_message(chat_id=message.chat.id, text='/start')
        else:
            await bot.send_message(chat_id=message.chat.id, text=f'Assalomu alaykum! {message.from_user.full_name}\nSiz botimizda eskisiz!')
