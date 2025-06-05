import app
from aiogram import Router
from aiogram import types
from aiogram.fsm.context import FSMContext
from ...modelml.fitmodel import predict
from .keyboards_message import MyStates
from ...parse_url.parsing import fetch_content

router = Router()

@router.message(MyStates.waiting_for_text)
async def handle_text_input(message: types.Message, state: FSMContext):
    user_text = message.text
    predicted = predict(user_text)
    
    if predicted == 1:
        predicted = "Вероятнее всего вас обманывают"
    else:
        predicted = "Скорее всего это правда!"
    
    await message.answer(predicted)
    await state.clear() 
    
@router.message(MyStates.waiting_for_url)
async def handle_text_input(message: types.Message, state: FSMContext):
    user_text = message.text
    article_content = await fetch_content(user_text)
    
    if article_content == app.error_message:
        predicted = app.error_message
    else:
        predicted = predict(article_content)
        
        if predicted == 1:
            predicted = "Вероятнее всего вас обманывают"
        else:
            predicted = "Скорее всего это правда!"
    
    await message.answer(predicted)
    await state.clear()  