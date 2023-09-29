from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


confirmation_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🔙 Ortga', callback_data="con:back"),
            InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="con:confirmation")
        ]
    ]
)


confirmation_button2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🔙 Ortga', callback_data="con:back"),
            InlineKeyboardButton(text="🗑 O'chirish", callback_data="con:delete")
        ]
    ]
)

confirmation_send_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🔙 Ortga', callback_data="con:back"),
            InlineKeyboardButton(text="✅ Jo'natish", callback_data="con:send")
        ]
    ]
)