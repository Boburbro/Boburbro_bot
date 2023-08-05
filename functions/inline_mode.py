from googletrans import Translator
from function import get_tr
def inline_BOT(text):
    if text[:2] == 'kl': # kril latin bot
        text1='Tarjimani yuborish'
        text2=get_tr(text[3:])
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
    else:
        text1="404 ERROR"
        text2="@TCTuzb kanaliga obuna bo'ling"
    
    
    return text1, text2