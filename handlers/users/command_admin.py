from loader import bot
from telebot.types import Message
from data.config import ADMINS
from functions.function import isAdmin

@bot.message_handler(commands=['admin'])
async def command_admin(message: Message):
    if isAdmin(message.chat.id):
        await bot.send_message(chat_id=message.chat.id, text="Admin panel")
    else:
        await bot.send_message(chat_id = message.chat.id, text = "Admin: @TCTuzb")