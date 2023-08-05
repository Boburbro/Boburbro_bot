print('ISHLAMOQDA...')
from loader import bot 
print('Loader qo\'shildi')
import asyncio
print('Asynico qo\'shildi')
import middlewares
print('Middlewares qo\'shildi')
import handlers
print('Handlers qo\'shildi')
import utils
print('Utils qo\'shildi')
print('+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#')

asyncio.run(bot.infinity_polling(skip_pending=True))