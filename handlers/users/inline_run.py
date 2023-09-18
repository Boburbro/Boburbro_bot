import telebot
from telebot import types
from loader import bot 
from functions.inline_mode import inline_BOT



@bot.inline_handler(lambda query: len(query.query) > 0)
async def query_text(inline_query):
    text = inline_BOT(inline_query.query)
    try:
        r = types.InlineQueryResultArticle('1', f'{text[0]}', types.InputTextMessageContent(f'{text[1]}', parse_mode="markdown"))
        await bot.answer_inline_query(inline_query.id, [r])

    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: len(query.query) == 0)
async def query_text(inline_query):
    try:
        helper=f"""
Assalomu alaykum.
Inline modemdan foydalanish uchun `@Boburbrobot [key] [text]` larni yozing.
`key` larni bilib olish uchun `@Boburbrobot key` ni kiriting.
@TCTuzb kanaliga obuna bo'ling!
"""
        r = types.InlineQueryResultArticle('1', 'Help', types.InputTextMessageContent(f'{helper}', parse_mode="markdown"))
        await bot.answer_inline_query(inline_query.id, [r])

    except Exception as e:
        print(e)

