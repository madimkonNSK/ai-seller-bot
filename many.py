import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
import asyncio

load_dotenv()
bot = Bot(token=os.getenv("7684985741:AAETWxsJ1rj8v2b6U3-9-U8z4dRTtZq2NZk"))
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer("Бот работает в Codespaces!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
