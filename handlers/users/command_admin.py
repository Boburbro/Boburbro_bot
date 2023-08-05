from loader import bot
from telebot.types import Message
from data.config import ADMINS
from functions.function import isAdmin
from keyboards.default.admin_button import admin_markup1

@bot.message_handler(commands=['admin'])
async def command_admin(message: Message):
    if isAdmin(message.chat.id):
        await bot.send_message(chat_id=message.chat.id, text="Admin panel", reply_markup=admin_markup1)
    else:
        await bot.send_message(chat_id = message.chat.id, text = "Admin: @TCTuzb")