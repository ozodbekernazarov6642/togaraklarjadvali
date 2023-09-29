import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data import config
from data.config import ADMINS
from keyboards.default.admin_button import admin_menu
from states.Admin_state import Admin_state

from data.list import app_info, days, updates_days
from loader import dp, bot
from data.week_day import monday, tuesday, wednesday, thursday, friday, saturday
from keyboards.inline.science_name_inline import science




def day_generator(days):
    result = ", ".join(days)
    return result


@dp.callback_query_handler(text='confirmation', state=Admin_state.add_week_day, user_id=ADMINS)
async def day_confirmation(call: types.CallbackQuery):
    if days:
        app_info["day"] = day_generator(days)
        await call.message.answer("Fanni tanlang ", reply_markup=science)
        await call.message.delete()
        await Admin_state.choose_subject.set()
        updates_days[monday] = monday
        updates_days[tuesday] = tuesday
        updates_days[wednesday] = wednesday
        updates_days[thursday] = thursday
        updates_days[friday] = friday
        updates_days[saturday] = saturday
    else:
        await call.answer("❌ Fan tanalnmadi", show_alert=True)


@dp.callback_query_handler(state=Admin_state.add_week_day, user_id=ADMINS)
async def day(call: types.CallbackQuery):
    day = call.data
    if day.endswith("✅"):
        edited_day = day.split("✅")[0]
        del days[edited_day]
        await call.answer("❌Hafta kuni o`chirildi")
        updates_days[edited_day] = edited_day
        keyboard_1 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=updates_days.get(monday), callback_data=updates_days.get(monday)),
                    InlineKeyboardButton(text=updates_days.get(tuesday), callback_data=updates_days.get(tuesday)),
                ],
                [
                    InlineKeyboardButton(text=updates_days.get(wednesday), callback_data=updates_days.get(wednesday)),
                    InlineKeyboardButton(text=updates_days.get(thursday), callback_data=updates_days.get(thursday)),
                ],
                [
                    InlineKeyboardButton(text=updates_days.get(friday), callback_data=updates_days.get(friday)),
                    InlineKeyboardButton(text=updates_days.get(saturday), callback_data=updates_days.get(saturday)),
                ],
                [
                    InlineKeyboardButton(text="🔙 Ortga", callback_data="week:back"),
                    InlineKeyboardButton(text="✅ Tanladim", callback_data="confirmation")
                ]
            ]
        )
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=keyboard_1)
    else:
        days[day] = day
        edited_day = f"{day}✅"
        updates_days[day] = edited_day
        updates_days[edited_day] = edited_day
        await call.answer("✅ Hafta kuni tanlandi")
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=updates_days.get(monday), callback_data=updates_days.get(monday)),
                    InlineKeyboardButton(text=updates_days.get(tuesday), callback_data=updates_days.get(tuesday)),
                ],
                [
                    InlineKeyboardButton(text=updates_days.get(wednesday), callback_data=updates_days.get(wednesday)),
                    InlineKeyboardButton(text=updates_days.get(thursday), callback_data=updates_days.get(thursday)),
                ],
                [
                    InlineKeyboardButton(text=updates_days.get(friday), callback_data=updates_days.get(friday)),
                    InlineKeyboardButton(text=updates_days.get(saturday), callback_data=updates_days.get(saturday)),
                ],
                [
                    InlineKeyboardButton(text="🔙 Ortga", callback_data="week:back"),
                    InlineKeyboardButton(text="✅ Tanladim", callback_data="confirmation")
                ]
            ]
        )
        await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            reply_markup=keyboard)
