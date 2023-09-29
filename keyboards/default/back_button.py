from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔙 Ortga")
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)


back_back_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔙 Ortga"),
            KeyboardButton(text="🔝 Bosh Menyu")
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)
