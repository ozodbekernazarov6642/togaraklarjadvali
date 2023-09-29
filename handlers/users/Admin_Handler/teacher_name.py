import re

from aiogram import types
from data.config import ADMINS
from keyboards.default.back_button import back
from keyboards.inline.time_inline import time
from states.Admin_state import Admin_state
from data.list import app_info, days
from loader import dp


@dp.callback_query_handler(state=Admin_state.choose_subject, user_id=ADMINS)
async def teacher_name(call: types.CallbackQuery):
    app_info['subject_name'] = call.data.split(':')[1]
    await call.answer("✅ Fan tanlandi")
    days.clear()
    await call.message.delete()
    await call.message.answer("To'garak nomini kiriting ✍🏻", reply_markup=back)
    await Admin_state.next()


@dp.message_handler(state=Admin_state.circle_name, user_id=ADMINS)
async def circle_name(message: types.Message):
    app_info['circle_name'] = message.text
    await message.answer("👨🏻‍🏫To'garak o'qituvchisini F.i.SH kiriting\n"
                             "Namuna: <code><b>O'taganov Bobur Alisher o'g'li</b></code>", reply_markup=back)
    await Admin_state.next()


@dp.message_handler(state=Admin_state.teacher_name, user_id=ADMINS)
async def teacher_name(message: types.Message):
    pattern = r"(?:[A-Za-z']+ [A-Z][a-z]+\s[A-Z][a-z]+)|(?:[A-Za-z']+ [A-Z ]'?[a-z]+)"
    if re.match(pattern, message.text):
        app_info["teacher_name"] = message.text
        await message.answer("To'garakni boshlanish vaqti 🕠", reply_markup=time)
        await Admin_state.next()
    else:
        await message.reply("F.I.SH Namunaga binoan to'ldiring‼️")




