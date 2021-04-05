from misc import token
from yobit import get_btc
from datetime import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет!\nНапиши или нажми "/btc" и я пришлю тебе текущий курс биткоина!')


@dp.message_handler(commands=['btc'])
async def btc_level(message: types.Message):
    try:
        await message.reply(f"***{datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                            f'Текущий курс - {get_btc()}'
                            )
    except:
        await message.reply('\U00002620 Ошибочка! Повтори попозже. \U00002620')


if __name__ == '__main__':
    executor.start_polling(dp)
