# 

from loader import bot 
from telebot.types import Message
from data.config import link

@bot.message_handler(commands=['links'])
async def command_help(message: Message):
    
    text=f"""
{link}CryLat - Kril -> Lotin, Lotin -> Kril
{link}Pulkiritish - Pul Kiritish
{link}fikr - Fikr bildirish
"""
    await bot.send_message(chat_id = message.chat.id, text = f"{text}")