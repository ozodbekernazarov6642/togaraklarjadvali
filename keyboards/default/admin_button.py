from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗒 ️To'garak Qo'shish"),
            KeyboardButton(text="🔍 Qidirish")
        ],
        [
            KeyboardButton(text="👨‍🎓 O'quvchilarga xabar yuborish 📤"),
            KeyboardButton(text="🗑 To'garakni o'chirish")
        ],
    ], resize_keyboard=True, one_time_keyboard=True
)
