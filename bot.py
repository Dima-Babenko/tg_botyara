import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils import executor

TOKEN = "YOUR_BOT_TOKEN"
WEB_APP_URL = "https://your-web-app-url.com"  # Замініть на свій хостинг

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Відкрити", web_app=WebAppInfo(url=WEB_APP_URL))
    )
    await message.answer("Натисни, щоб відкрити застосунок:", reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)