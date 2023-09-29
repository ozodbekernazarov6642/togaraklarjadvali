import re

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.default.back_button import back
from keyboards.inline.Confirmation import confirmation_button
from keyboards.inline.time_inline import time
from states.Admin_state import Admin_state
from data.list import app_info
from loader import dp

times = {"1400": ["14:00", "1400"], "1430": ["14:30", "1430"], "1500": ["15:00", "1500"], "1530": ["15:30", "1530"],
         "1600": ["16:00", "1600"], "1630": ["16:30", "1630"]}


@dp.callback_query_handler(state=Admin_state.start_time, user_id=ADMINS)
async def finish_time(call: types.CallbackQuery):
    app_info["start_time"] = call.data
    keyboard_time = InlineKeyboardMarkup(row_width=2)
    if call.data == '1630':
        await call.answer("Iltimos boshqa vaqtni tanlang ‼️")
    else:
        for ktime, vtime in times.items():
            if int(call.data) < int(ktime):
                keyboard_time.add(InlineKeyboardButton(text=vtime[0], callback_data=vtime[1]))
        keyboard_time.add(InlineKeyboardButton(text="🔙 Ortga", callback_data="finish_time:back"))
        await call.message.answer("To'garak tugash vaqti 🕠", reply_markup=keyboard_time)
        await call.message.delete()
        await Admin_state.next()


@dp.callback_query_handler(state=Admin_state.finish_time, user_id=ADMINS)
async def finish_time_(call: types.CallbackQuery):
    app_info["finish_time"] = call.data
    if app_info['start_time'] == "1400":
        app_info['start_time'] = "14:00"
    if app_info['start_time'] == "1430":
        app_info['start_time'] = "14:30"
    if app_info['start_time'] == "1500":
        app_info['start_time'] = "15:00"
    if app_info['start_time'] == "1530":
        app_info['start_time'] = "15:30"
    if app_info['start_time'] == "1600":
        app_info['start_time'] = "16:00"
    if app_info['start_time'] == "1630":
        app_info['start_time'] = "16:30"
    if app_info['finish_time'] == "1400":
        app_info['finish_time'] = "14:00"
    if app_info['finish_time'] == "1430":
        app_info['finish_time'] = "14:30"
    if app_info['finish_time'] == "1500":
        app_info['finish_time'] = "15:00"
    if app_info['finish_time'] == "1530":
        app_info['finish_time'] = "15:30"
    if app_info['finish_time'] == "1600":
        app_info['finish_time'] = "16:00"
    if app_info['finish_time'] == "1630":
        app_info['finish_time'] = "16:30"

    info = (f"🔰 To'garak nomi: {app_info['circle_name']}\n\n"
            f"📚 To'garak fani: {app_info['subject_name']}\n\n"
            f"👨‍🏫 To'garak o'qituvchisi: {app_info['teacher_name']}\n\n"
            f"🗓 To'garak kunlari: {app_info['day']}\n\n"
            f"🕐 To'garak boshlanish vaqti: {app_info['start_time']}\n\n"
            f"🕠 To'garak tugash vaqti: {app_info['finish_time']}")
    await call.message.answer(info, reply_markup=confirmation_button)
    await Admin_state.next()
    await call.message.delete()
