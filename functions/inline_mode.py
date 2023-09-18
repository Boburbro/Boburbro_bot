from googletrans import Translator
from functions.function import showGR

def get_tr(text):
    """Kril->Latin, Latin->Kril"""
    from transliterate import to_cyrillic, to_latin
    if text.isascii():
        return (to_cyrillic(text))
    else:
        return (to_latin(text))

def inline_BOT(text):
    if text[:2] == 'kl': # kril latin bot
        text1='Tarjimani yuborish'
        text2=get_tr(text[3:])
    elif text == "key":
        text1 = "'Key'larni olish"
        text2="""
Tarjimon:
    `uzen` [text] - O'zbekdan Ingliz tiliga
    `enuz` [text] - Inglizdan O'zbek tiliga
    `uzru` [text] - O'zbekdan Rus tiliga
    `ruuz` [text] - Rusdan O'zbek tiliga
    `kl` [text] - Krildan lotinga, lotindam krilga
"""
    elif text == "help":
        text1='help'
        text2="""
Assalomu alaykum.
Inline modemdan foydalanish uchun `@Boburbrobot [key] [text]` larni yozing.
`key` larni bilib olish uchun `@Boburbrobot key` ni kiriting.
@TCTuzb kanaliga obuna bo'ling!
"""
    elif text == 'pk' or text == 'kr':
        text1 = 'Kartani yuborish'
        text2 = 'Karta raqam:\n\n8600052938509880\nYM'
    elif text[:4] == 'uzen':
        tarjimon = Translator() 
        matn_uz = f"{text[5:]}"
        tarjima = tarjimon.translate(matn_uz, src='uz' , dest='en')
        text1='Tarjimani yuborish'
        text2 = tarjima.text
    elif text[:4] == 'uzru':
        tarjimon = Translator() 
        matn_uz = f"{text[5:]}"
        tarjima = tarjimon.translate(matn_uz, src='uz' , dest='ru')
        text1='Tarjimani yuborish'
        text2 = tarjima.text
    elif text[:4] == 'enuz':
        tarjimon = Translator() 
        matn_uz = f"{text[5:]}"
        tarjima = tarjimon.translate(matn_uz, src='en' , dest='uz')
        text1='Tarjimani yuborish'
        text2 = tarjima.text
    elif text[:4] == 'ruuz':
        tarjimon = Translator() 
        matn_uz = f"{text[5:]}"
        tarjima = tarjimon.translate(matn_uz, src='ru' , dest='uz')
        text1='Tarjimani yuborish'
        text2 = tarjima.text
    elif text== "gr":
        print(1)
        text1 = 'Guruhlarni yuborish'
        text2 = showGR()
    
    

    else:
        text1="404 ERROR"
        text2="@TCTuzb kanaliga obuna bo'ling"
    
    
    return text1, text2