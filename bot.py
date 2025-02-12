import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = "Т7916345622:AAHPfQLpnAbjbGMy8McaVLh1mXZ_RGk_yJs"
WEB_APP_URL = "https://dima-babenko.github.io/tg_botyara/"

# Включаємо логування
logging.basicConfig(level=logging.INFO)

# Створюємо бот і диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обробник команди /start
@dp.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Відкрити WebApp", web_app=WebAppInfo(url=WEB_APP_URL))]
    ])
    await message.answer("Натисни кнопку нижче, щоб відкрити застосунок:", reply_markup=keyboard)

async def main():
    dp.include_router(dp)  # Додаємо роутер
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
