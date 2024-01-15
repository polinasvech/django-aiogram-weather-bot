import asyncio
import json
import logging
import os

import requests
from aiogram import Bot, Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart

logger = logging.getLogger(__name__)

TOKEN = os.environ.get("TOKEN")
API_HOST = os.environ.get("API_HOST", None)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    """
    Обработка команды `/start`
    """
    kb = [
        [types.KeyboardButton(text="Узнать погоду")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Нажми на кнопку - получишь результат", reply_markup=keyboard)


@dp.message(F.text.lower() == "узнать погоду")
async def get_weather(message: types.Message):
    await message.reply("Введите название города")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        weather_info = requests.get(f" http://{API_HOST}:8000/weather?city={message.text}")
        if weather_info.status_code == 200:
            weather_info = json.loads(weather_info.content)
            await message.reply(f"{weather_info['temperature']} \n{weather_info['pressure']} \n{weather_info['wind_speed']}")
        else:
            error_msg = json.loads(weather_info.content.decode("utf-8"))
            await message.reply(error_msg["detail"])
    except TypeError:
        await message.answer("Что-то пошло не так :(")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logger.setLevel(logging.INFO)
    asyncio.run(main())
