import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "ТВОЙ_ТОКЕН"  # Замініть на ваш реальний токен
WEBAPP_URL = "https://твій-юзернейм.github.io/tg_webapp_project/webapp/"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def start(message: types.Message):
    if message.text == "/start":
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔗 Відкрити WebApp", web_app=types.WebAppInfo(url=WEBAPP_URL))]
        ])
        
        await message.answer("Натисни кнопку, щоб відкрити застосунок:", reply_markup=keyboard)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())