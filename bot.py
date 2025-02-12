import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.filters import Command
from flask import Flask, render_template

TOKEN = "7916345622:AAHPfQLpnAbjbGMy8McaVLh1mXZ_RGk_yJs"
WEB_APP_URL = "https://dima-babenko.github.io/tg_botyara/"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

# === Бот обробляє команду /start ===
@dp.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Відкрити WebApp", web_app=WebAppInfo(url=WEB_APP_URL))]
    ])
    await message.answer("Натисни кнопку нижче, щоб відкрити застосунок:", reply_markup=keyboard)

# === Запуск Flask-сервера ===
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("templates/index.html") 

async def main():
    dp.include_router(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Запускаємо Flask у окремому потоці
    from threading import Thread
    Thread(target=lambda: app.run(host="0.0.0.0", port=5000, debug=True)).start()

    # Запускаємо бота
    asyncio.run(main())