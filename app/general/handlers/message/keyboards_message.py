from aiogram import Router
from aiogram import F, types
from aiogram.types import Message

router = Router()

@router.message(F.text.lower() == "ссылкой на статью")
async def url_info(message: types.Message):
    pass

@router.message(F.text.lower() == "текстом в сообщении")
async def url_info(message: types.Message):
    pass