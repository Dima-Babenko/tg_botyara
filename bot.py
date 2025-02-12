import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

TOKEN = "7916345622:AAHPfQLpnAbjbGMy8McaVLh1mXZ_RGk_yJs"  # Встав свій токен від BotFather
WEBAPP_URL = "https://dima-babenko.github.io/tg_botyara/"  # Посилання на твою WebApp

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    webapp_button = InlineKeyboardButton("Відкрити WebApp", web_app=types.WebAppInfo(url=WEBAPP_URL))
    keyboard.add(webapp_button)
    
    await message.answer("Натисни кнопку, щоб відкрити WebApp:", reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)