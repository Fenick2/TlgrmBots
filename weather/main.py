import requests
from TlgrmBots.weather.config import token
from datetime import datetime


def get_weather(city, token):
    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&lang=ru&units=metric'
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
        print(f"Погода в г.{city}:", f'Температура: {temp} °C',
              f'Ощущается как: {feels_like} °C', f'Влажность: {humidity} %', f'Давление: {pressure} гПа',
              f'Облачность: {desc}', f'Скорость ветра: {wind} м/с', f'Восход: {sunrise}', sep='\n')

    except Exception as ex:
        print(ex)
        print('Проверьте название города!')


def main():
    city = input('Введите название города: ')
    get_weather(city, token)


if __name__ == '__main__':
    main()
