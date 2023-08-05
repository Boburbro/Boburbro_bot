from telebot.asyncio_filters import StateFilter
from loader import bot 
from states.state1 import STATE1_
from states.state2 import STATE2_
from telebot.types import Message
from functions.function import get_tr,addFIKR,addMQ
from keyboards.inline.button1 import InlineMatkup1
from keyboards.default.button_start import markup1

@bot.message_handler(state=STATE1_.State1)
async def sdfgh(message: Message):
    text = get_tr(message.text)
    text+='\n\n@TCTuzb'
    await bot.send_message(message.chat.id, text)



@bot.message_handler(state=STATE2_.State1)
async def sdfdgh(message: Message):
    fikr = message.text
    await bot.send_message(chat_id='-1001835678238', text=fikr+f'\n\nid: {message.chat.id, message.from_user.id}')
    await bot.send_message(chat_id=message.chat.id, text='Fikringiz uchun raxmat. Botni baxolang!', reply_markup=InlineMatkup1)
    await bot.set_state(chat_id=message.chat.id, user_id=message.from_user.id, state=STATE2_.State2)



@bot.callback_query_handler(func=lambda call: True, state=STATE2_.State2)
async def inline_query(call):
    try:
        await bot.delete_state(user_id=call.message.from_user.id, chat_id=call.message.chat.id)
        addFIKR()
        addMQ(str(call.data))
    except Exception as e:
        print(e)
    await bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
    await bot.send_message(chat_id=call.message.chat.id, text='Bosh menu', reply_markup=markup1 ) 





bot.add_custom_filter(StateFilter(bot))