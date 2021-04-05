import requests
from datetime import datetime
from config import tg_token, token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет!\nНапиши название города и я пришлю сводку погоды!')


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={token}&lang=ru&units=metric'
        )
        data = r.json()

        city = data['name']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
        desc = data['weather'][0]['description']

        await message.reply(f"***{datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                            f"Погода в г.{city}:\nТемпература: {temp} °C\n"
                            f"Ощущается как: {feels_like} °C\nВлажность: {humidity} %\nДавление: {pressure} гПа\n"
                            f"Облачность: {desc}\nСкорость ветра: {wind} м/с\nВосход: {sunrise}\n"
                            f"***Хорошего дня!***"
                            )

    except:
        await message.reply('\U00002620 Проверь название города! \U00002620')


if __name__ == '__main__':
    executor.start_polling(dp)
