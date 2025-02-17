import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command


TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
logging.basicConfig(filename="Info.txt", level=logging.INFO)


@dp.message(Command(commands=['start']))
async def start(message: Message):
    name = message.from_user.first_name
    name_id = message.from_user.id
    logging.info(f'{name} запустил бота {name_id}')
    await message.reply(f"Привет, {name},\nчтобы продолжить введи ФИО")


@dp.message()
async def Fio(message: Message):
    text = message.text
    text2 = text_translite(text)
    await message.answer(text=text2)
  
DIKT = {'А':'A', 'Б':'B', 'В':'V', 'Г':'G', 'Д':'D', 'Е':'E', 'Ё':'E',
          'Ж':'ZH', 'З':'Z', 'И':'I', 'Й':'I', 'К':'K', 'Л':'L', 'М':'M',
          'Н':'N', 'О':'O', 'П':'P', 'Р':'R', 'С':'S', 'Т':'T', 'У':'U',
          'Ф':'F', 'Х':'KH', 'Ц':'TS', 'Ч':'CH', 'Ш':'SH', 'Щ':'SHCH', 
          'Ы':'Y', 'Ъ':'IE', 'Э':'E', 'Ю':'IU', 'Я':'IA'}   


def text_translite(text):
    text_translite = []
    text = text.upper().split()
    if len(text) > 3:
        return ('Неккоректный ввод!')
    else:
        for i in text:
            for z in i:
                if z in DIKT:
                    i = i.replace(z, DIKT[z])
            text_translite.append(i.lower())
    return (' '.join(text_translite).title())

if __name__ == '__main__':
    dp.run_polling(bot)