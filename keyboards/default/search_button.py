from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

search_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 To'garak fani orqali"),
            KeyboardButton(text="📆 Hafta kuni orqali")
        ],
        [
            KeyboardButton(text="🔙 Ortga")
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)


search_button_user = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 To'garak fani orqali"),
            KeyboardButton(text="📆 Hafta kuni orqali")
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)
