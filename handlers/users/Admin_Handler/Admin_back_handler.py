import types

from aiogram import types
from aiogram.dispatcher import FSMContext
from data.week_day import monday, tuesday, wednesday, thursday, friday, saturday
from data.list import days, updates_days
from data.list import updates_days
from keyboards.default.search_button import search_button
from keyboards.inline.science_name_inline import science
from keyboards.inline.time_inline import time
from states.Admin_state import Admin_state, Admin_search, Admin_delete, Admin_all_user
from keyboards.default.admin_button import admin_menu
from keyboards.inline.admin_weekdays import week_days, week_days2
from keyboards.default.back_button import back
from loader import dp
from data import config


@dp.message_handler(text="🔙 Ortga", state=Admin_state.circle_name, user_id=config.ADMINS)
async def back_(message: types.Message):
    await message.delete()
    await message.answer("Fanni tanlang ", reply_markup=science)
    await Admin_state.previous()


@dp.callback_query_handler(text='week:back', state=Admin_state.add_week_day, user_id=config.ADMINS)
async def inline_back(call: types.CallbackQuery, state=FSMContext):
    days.clear()
    updates_days[monday] = monday
    updates_days[tuesday] = tuesday
    updates_days[wednesday] = wednesday
    updates_days[thursday] = thursday
    updates_days[friday] = friday
    updates_days[saturday] = saturday
    await call.message.delete()
    await call.message.answer(f"Tugmalardan birini tanlang👇", reply_markup=admin_menu)
    await Admin_state.previous()


@dp.callback_query_handler(text="science:back", state=Admin_state.choose_subject, user_id=config.ADMINS)
async def science_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("To'garak kunlarini qo'shing👇", reply_markup=week_days)
    await Admin_state.add_week_day.set()


@dp.message_handler(text="🔙 Ortga", state=Admin_state.teacher_name, user_id=config.ADMINS)
async def teacher_back(message: types.Message):
    await message.delete()
    await message.answer("To'garak nomini kiriting ✍🏻", reply_markup=back)
    await Admin_state.previous()


@dp.callback_query_handler(text="time:back", state=Admin_state.start_time, user_id=config.ADMINS)
async def time_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("👨🏻‍🏫To'garak o'qituvchisini F.i.SH kiriting\n"
                              "Namuna: <code><b>O'taganov Bobur Alisher o'g'li</b></code>", reply_markup=back)
    await Admin_state.previous()


@dp.message_handler(text="🔙 Ortga", state=Admin_state.start_time, user_id=config.ADMINS)
async def time_default_back(message: types.Message):
    await message.delete()
    await message.answer("👨🏻‍🏫To'garak o'qituvchisini F.i.SH kiriting\n"
                         "Namuna: <code><b>O'taganov Bobur Alisher o'g'li</b></code>", reply_markup=back)
    await Admin_state.previous()


@dp.callback_query_handler(text="finish_time:back", state=Admin_state.finish_time, user_id=config.ADMINS)
async def finish_time_back(call: types.CallbackQuery):
    await call.message.answer("To'garakni boshlanish vaqti 🕠", reply_markup=time)
    await Admin_state.previous()
    await call.message.delete()


@dp.message_handler(text="🔙 Ortga", state=Admin_state.finish_time, user_id=config.ADMINS)
async def teacher_back(message: types.Message):
    await message.answer("To'garakni boshlanish vaqti 🕠", reply_markup=time)
    await Admin_state.previous()
    await message.delete()


@dp.callback_query_handler(text="con:back", state=Admin_state.confirmation, user_id=config.ADMINS)
async def confirmation_time_back(call: types.CallbackQuery):
    await call.message.answer("To'garakni boshlanish vaqti 🕠", reply_markup=time)
    await Admin_state.start_time.set()
    await call.message.delete()


@dp.message_handler(text="🔙 Ortga", state=Admin_state.confirmation, user_id=config.ADMINS)
async def teacher_back(message: types.Message):
    await message.answer("To'garakni boshlanish vaqti 🕠", reply_markup=time)
    await Admin_state.start_time.set()
    await message.delete()


@dp.message_handler(text="🔙 Ortga", state=Admin_search.week_search, user_id=config.ADMINS)
async def week_search_back(message: types.Message):
    await message.answer('📆 Hafta kunini tanlang', reply_markup=week_days2)
    await Admin_search.week_search.set()
    await message.delete()


@dp.message_handler(text="🔙 Ortga", state=Admin_search.subject_search, user_id=config.ADMINS)
async def sub_search_back(message: types.Message):
    await message.answer("To'garak fanini tanlang 👇", reply_markup=science)
    await Admin_search.subject_search.set()
    await message.delete()


@dp.callback_query_handler(text="week:back", state=Admin_search.week_search, user_id=config.ADMINS)
@dp.callback_query_handler(text="science:back", state=Admin_search.subject_search, user_id=config.ADMINS)
async def sub_back(call: types.CallbackQuery):
    await call.message.answer("Qidirish turini tanlang 🤳", reply_markup=search_button)
    await Admin_search.menu_search.set()
    await call.message.delete()


@dp.message_handler(text="🔙 Ortga", state=Admin_search.menu_search, user_id=config.ADMINS)
async def menu_back1(message: types.Message, state: FSMContext):
    await message.answer(f"Tugmalardan birini tanlang👇", reply_markup=admin_menu)
    await message.delete()
    await state.finish()


@dp.message_handler(text="🔙 Ortga", state=Admin_delete.circle_delete, user_id=config.ADMINS)
async def menu_back2(message: types.Message, state: FSMContext):
    await message.answer(f"Tugmalardan birini tanlang👇", reply_markup=admin_menu)
    await message.delete()
    await state.finish()


@dp.callback_query_handler(text="con:back", state=Admin_delete, user_id=config.ADMINS)
async def confirmation_delete_back(call: types.CallbackQuery):
    await call.message.answer("🗑 O'chirish ko'dini kiriting", reply_markup=back)
    await Admin_delete.circle_delete.set()
    await call.message.delete()


@dp.message_handler(text="🔙 Ortga", state=Admin_all_user.input_message, user_id=config.ADMINS)
async def send_message_back(message: types.Message, state: FSMContext):
    await message.answer(f"Tugmalardan birini tanlang👇", reply_markup=admin_menu)
    await message.delete()
    await state.finish()


@dp.callback_query_handler(text="con:back", state=Admin_all_user.confirmation_message, user_id=config.ADMINS)
async def message_back(call: types.CallbackQuery):
    await call.message.answer("Xabar matnini yozing ✍🏻", reply_markup=back)
    await call.message.delete()
    await Admin_all_user.input_message.set()