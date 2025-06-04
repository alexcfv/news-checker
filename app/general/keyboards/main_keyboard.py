from aiogram import types
kb = [
        [
            types.KeyboardButton(text="ссылкой на статью"),
            types.KeyboardButton(text="текстом в сообщении")
        ],
]

keyboard = types.ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    input_field_placeholder="Выберите способ отправки"
)