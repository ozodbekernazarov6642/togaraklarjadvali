from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.week_day import monday, tuesday, wednesday, thursday, friday, saturday

week_days = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=monday, callback_data=monday),
            InlineKeyboardButton(text=tuesday, callback_data=tuesday)
        ],
        [
            InlineKeyboardButton(text=wednesday, callback_data=wednesday),
            InlineKeyboardButton(text=thursday, callback_data=thursday)
        ],
        [
            InlineKeyboardButton(text=friday, callback_data=friday),
            InlineKeyboardButton(text=saturday, callback_data=saturday)
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="week:back"),
            InlineKeyboardButton(text="✅ Tanladim", callback_data="confirmation")
        ]
    ]
)

week_days2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=monday, callback_data=f"week:{monday}"),
            InlineKeyboardButton(text=tuesday, callback_data=f"week:{tuesday}")
        ],
        [
            InlineKeyboardButton(text=wednesday, callback_data=f"week:{wednesday}"),
            InlineKeyboardButton(text=thursday, callback_data=f"week:{thursday}")
        ],
        [
            InlineKeyboardButton(text=friday, callback_data=f"week:{friday}"),
            InlineKeyboardButton(text=saturday, callback_data=f"week:{saturday}")
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="week:back")
        ]
    ]
)
