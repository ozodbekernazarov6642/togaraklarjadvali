from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

time = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="14:00", callback_data="1400"),
            InlineKeyboardButton(text="14:30", callback_data="1430")
        ],
        [
            InlineKeyboardButton(text="15:00", callback_data="1500"),
            InlineKeyboardButton(text="15:30", callback_data="1530")
        ],
        [
            InlineKeyboardButton(text="16:00", callback_data="1600"),
            InlineKeyboardButton(text="16:30", callback_data="1630")
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="time:back")
        ]
    ]
)
