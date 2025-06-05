from aiogram import Router
from aiogram import F
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class MyStates(StatesGroup):
    waiting_for_text = State()
    waiting_for_url = State()

router = Router()

@router.message(F.text.lower() == "ссылкой на статью")
async def url_info(message: Message, state: FSMContext):
    await message.answer("Введите ссылку:")
    await state.set_state(MyStates.waiting_for_url)

@router.message(F.text.lower() == "текстом в сообщении")
async def text_info(message: Message, state: FSMContext):
    await message.answer("Введите текст:")
    await state.set_state(MyStates.waiting_for_text)
