

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.search_button import search_button_user
from loader import dp, db, db1
from states.User_state import user_state



@dp.message_handler(CommandStart(), state=user_state.science)
@dp.message_handler(CommandStart(), state=user_state.week_search)
async def state_start(message: types.Message, state: FSMContext):
    await message.answer(f"<b>Salom {message.from_user.full_name}</b>\n\n"
                         f"<i>To'garakni qidirish usulini tanlang🤳</i>", reply_markup=search_button_user)
    await state.finish()


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    try:
        db1.add_student(int(user_id), str(user_name))
        await message.answer(f"<b>Salom, {message.from_user.full_name}❗\n\n"
                             f"To'garaklar haqida ma'lumot olishingiz mumkin👇.</b>")
        await message.answer(f"<i>To'garakni qidirish usulini tanlang🤳</i>", reply_markup=search_button_user)
    except:
        await message.answer(f"<b>Salom {message.from_user.full_name}</b>\n\n"
                             f"<i>To'garakni qidirish usulini tanlang🤳</i>", reply_markup=search_button_user)


