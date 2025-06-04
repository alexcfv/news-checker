import app
import asyncio
import logging
from aiogram import Bot, Dispatcher
from app.general.handlers.message import start_message, keyboards_message

bot = Bot(token=app.api_key)
dp = Dispatcher()

dp.include_router(start_message.routerб, keyboards_message)

logging.basicConfig(level=app.logging_level)
    
async def main():
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())
