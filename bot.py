import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "YOUR_BOT_TOKEN"  # Замініть на свій токен
WEB_APP_URL = "https://dima-babenko.github.io/tg_botyara/"  # Замініть на свій сайт

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Відкрити", web_app=WebAppInfo(url=WEB_APP_URL))]
    ])
    await message.answer("Натисни кнопку, щоб відкрити застосунок:", reply_markup=keyboard)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)  # Видаляє невідправлені повідомлення
    await dp.start_polling(bot)  # Запуск бота

if __name__ == "__main__":
    asyncio.run(main())