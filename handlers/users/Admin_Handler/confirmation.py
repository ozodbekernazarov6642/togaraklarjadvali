import pytz
from aiogram import types
import datetime
from aiogram.dispatcher import FSMContext

from data.list import app_info
from states.Admin_state import Admin_state
from keyboards.default.admin_button import admin_menu
from keyboards.inline.admin_weekdays import week_days
from loader import dp, db
from data import config


@dp.callback_query_handler(text="con:confirmation", state=Admin_state.confirmation, user_id=config.ADMINS)
async def confirmation(call: types.CallbackQuery, state: FSMContext):
    now = datetime.datetime.now(pytz.timezone("Asia/Tashkent"))
    time1 = str(now).split('.')
    time = time1[1].split('+')[0] * 2
    db.add_circle(
        time, app_info['day'], app_info['circle_name'], app_info['subject_name'], app_info['teacher_name'],
        app_info['start_time'], app_info['finish_time']
    )
    await call.answer("✅ To'garak ma'lumotlari qo'shildi", show_alert=True)
    await call.message.delete()
    await call.message.answer("Tugmalardan birini tanlang👇", reply_markup=admin_menu)
    await state.finish()

