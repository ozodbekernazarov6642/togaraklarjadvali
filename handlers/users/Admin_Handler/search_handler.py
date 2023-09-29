from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.default.back_button import back
from keyboards.default.search_button import search_button
from keyboards.inline.science_name_inline import science
from states.Admin_state import Admin_state, Admin_search
from keyboards.default.admin_button import admin_menu
from keyboards.inline.admin_weekdays import week_days, week_days2
from loader import dp, db
from data import config


@dp.message_handler(text="🔍 Qidirish", user_id=config.ADMINS)
async def search(message: types.Message):
    await message.answer("Qidirish turini tanlang 🤳", reply_markup=search_button)
    await Admin_search.menu_search.set()
    await message.delete()


@dp.message_handler(text="📚 To'garak fani orqali", state=Admin_search.menu_search, user_id=config.ADMINS)
async def sub_search(message: types.Message):
    await message.answer("To'garak fanini tanlang 👇", reply_markup=science)
    await Admin_search.subject_search.set()
    await message.delete()


@dp.callback_query_handler(Text(startswith='science'), state=Admin_search.subject_search, user_id=config.ADMINS)
async def sen_info(call: types.CallbackQuery):
    sub = call.data.split(':')[1]
    circles = db.select_all_circle()
    status = None
    for circle in circles:
        if circle[3] == sub:
            response = (f"🔰 To'garak nomi: {circle[2]}\n\n"
                        f"📚 To'garak fani: {circle[3]}\n\n"
                        f"👨‍🏫 To'garak o'qituvchisi: {circle[4]}\n\n"
                        f"🗓 To'garak kunlari: {circle[1]}\n\n"
                        f"🕐 To'garak boshlanish vaqti: {circle[5]}\n\n"
                        f"🕠 To'garak tugash vaqti: {circle[6]}\n\n"
                        f"❌ O'chirish ko'di: <code>{circle[0]}</code>")
            await call.message.answer(response, reply_markup=back)
            status = True
            await call.message.delete()
    if status != True:
        await call.answer(f"❌ {sub} fan to'garak yo'q")
        await call.answer(cache_time=1)


@dp.message_handler(text="📆 Hafta kuni orqali", state=Admin_search.menu_search, user_id=config.ADMINS)
async def week_search(message: types.Message):
    await message.answer('📆 Hafta kunini tanlang', reply_markup=week_days2)
    await Admin_search.week_search.set()
    await message.delete()


@dp.callback_query_handler(Text(startswith="week"), state=Admin_search.week_search, user_id=config.ADMINS)
async def week_response(call: types.CallbackQuery):
    week_day = call.data.split(':')[1]
    days = db.select_all_circle()
    status = None
    for day_ in days:
        if day_[1] == week_day:
            response = (f"🔰 To'garak nomi: {day_[2]}\n\n"
                        f"📚 To'garak fani: {day_[3]}\n\n"
                        f"👨‍🏫 To'garak o'qituvchisi: {day_[4]}\n\n"
                        f"🗓 To'garak kunlari: {day_[1]}\n\n"
                        f"🕐 To'garak boshlanish vaqti: {day_[5]}\n\n"
                        f"🕠 To'garak tugash vaqti: {day_[6]}\n\n"
                        f"❌ O'chirish ko'di: <code>{day_[0]}</code>")
            await call.message.answer(response, reply_markup=back)
            status = True
            await call.answer(cache_time=5)
        elif week_day in day_[1]:
            response = (f"🔰 To'garak nomi: {day_[2]}\n\n"
                        f"📚 To'garak fani: {day_[3]}\n\n"
                        f"👨‍🏫 To'garak o'qituvchisi: {day_[4]}\n\n"
                        f"🗓 To'garak kunlari: {day_[1]}\n\n"
                        f"🕐 To'garak boshlanish vaqti: {day_[5]}\n\n"
                        f"🕠 To'garak tugash vaqti: {day_[6]}\n\n"
                        f"❌ O'chirish ko'di: <code>{day_[0]}</code>")
            await call.message.answer(response, reply_markup=back)
            await call.message.delete()
            status = True
            await call.answer(cache_time=5)
    if status != True:
        await call.answer(f"❌ {week_day} kuni to'garak yo'q")
        await call.answer(cache_time=1)
