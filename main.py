import app
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

bot = Bot(token=app.api_key)
dp = Dispatcher()

logging.basicConfig(level=app.logging_level)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply("Hello")
    
async def main():
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())
