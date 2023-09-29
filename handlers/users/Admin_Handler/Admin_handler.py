from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

from data.list import app_info, days
from states.Admin_state import Admin_state, Admin_search, Admin_delete, Admin_all_user
from keyboards.default.admin_button import admin_menu
from keyboards.inline.admin_weekdays import week_days
from loader import dp
from data import config


@dp.message_handler(CommandStart(), user_id=config.ADMINS)
async def admin_start(message: types.Message, state: FSMContext):
    await message.answer(f"Assalomu aleykum ustoz!\n"
                         f"Tugmalardan birini tanlang👇", reply_markup=admin_menu)
    days.clear()
    await state.finish()


@dp.message_handler(CommandStart(), state=Admin_all_user.input_message, user_id=config.ADMINS)
@dp.message_handler(CommandStart(), state=Admin_all_user.confirmation_message, user_id=config.ADMINS)
@dp.message_handler(CommandStart(), state=Admin_search.menu_search, user_id=config.ADMINS)
@dp.message_handler(CommandStart(), state=Admin_search.week_search, user_id=config.ADMINS)
@dp.message_handler(CommandStart(), state=Admin_search.subject_search, user_id=config.ADMINS)
@dp.message_handler(CommandStart(), state=Admin_delete.circle_delete, user_id=config.ADMINS)
@dp.message_handler(CommandStart(), state=Admin_delete.delete_confirmation, user_id=config.ADMINS)
@dp.message_handler(CommandStart(), state=Admin_state.add_week_day, user_id=config.ADMINS)
@dp.message_handler(CommandStart(), state=Admin_state.choose_subject, user_id=config.ADMINS)
@dp.message_handler(CommandStart(), state=Admin_state.circle_name, user_id=config.ADMINS)
@dp.message_handler(CommandStart(), state=Admin_state.teacher_name, user_id=config.ADMINS)
@dp.message_handler(CommandStart(), state=Admin_state.start_time, user_id=config.ADMINS)
@dp.message_handler(CommandStart(), state=Admin_state.finish_time, user_id=config.ADMINS)
@dp.message_handler(CommandStart(), state=Admin_state.confirmation, user_id=config.ADMINS)
async def admin_start(message: types.Message, state: FSMContext):
    await message.answer(f"Assalomu aleykum ustoz!\n"
                         f"Tugmalardan birini tanlang👇", reply_markup=admin_menu)
    await state.finish()


@dp.message_handler(text="🗒 ️To'garak Qo'shish")
async def circle_add(message: types.Message):
    await message.answer("To'garak kunlarini qo'shing👇", reply_markup=week_days)
    await Admin_state.add_week_day.set()

