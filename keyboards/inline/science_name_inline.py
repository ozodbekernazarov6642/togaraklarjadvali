from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


science = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Matematika", callback_data="science:Matematika"),
            InlineKeyboardButton(text="Rus tili", callback_data="science:Rus tili")
        ],
        [
            InlineKeyboardButton(text="Adabiyot", callback_data="science:Adabiyot"),
            InlineKeyboardButton(text="Ingliz tili", callback_data="science:Ingliz tili")
        ],
        [
            InlineKeyboardButton(text="Jismoniy tarbiya", callback_data="science:Jismoniy tarbiya"),
            InlineKeyboardButton(text="Tarix", callback_data="science:Tarix")
        ],
        [
            InlineKeyboardButton(text="Geografiya", callback_data="science:Geografiya"),
            InlineKeyboardButton(text="Musiqa", callback_data="science:Musiqa")
        ],
        [
            InlineKeyboardButton(text="Tasviriy san`at", callback_data="science:Tasviriy san'at"),
            InlineKeyboardButton(text="Texnologiya", callback_data="science:Texnalogiya")
        ],
        [
            InlineKeyboardButton(text="Biologiya", callback_data="science:Biologiya"),
            InlineKeyboardButton(text="Informatika", callback_data="science:Informatika")
        ],
        [
            InlineKeyboardButton(text="CHQBT", callback_data="science:CHQBT"),
            InlineKeyboardButton(text="Kimyo", callback_data="science:Kimyo")
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="science:back")
        ]
    ]
)