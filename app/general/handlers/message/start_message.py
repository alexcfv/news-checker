import app
from aiogram import types, Router
from aiogram.filters.command import Command
from keyboards.main_keyboard import keyboard

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(app.start_message, reply_markup=keyboard)