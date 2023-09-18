from loader import bot
from telebot.types import BotCommand
import asyncio

async def set_my_commands():
    await bot.set_my_commands([
        BotCommand('start', 'Botni qayta ishga tushirish'),
        BotCommand('help', 'Yordam olish'),
        BotCommand('admin', 'Admin bilan bog\'lanish'),
        BotCommand('links', 'Linklarni olish'),
    ])

asyncio.run(set_my_commands())