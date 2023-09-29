import asyncio
from aiogram import types
from data.config import ADMINS
from keyboards.default.admin_button import admin_menu
from keyboards.default.back_button import back
from keyboards.inline.Confirmation import confirmation_send_button
from states.Admin_state import Admin_all_user
from loader import dp, db1, bot


@dp.message_handler(text="👨‍🎓 O'quvchilarga xabar yuborish 📤", user_id=ADMINS)
async def all_send(message: types.Message):
    await message.answer("Xabar matnini yozing ✍🏻", reply_markup=back)
    await Admin_all_user.input_message.set()


@dp.message_handler(state=Admin_all_user.input_message, content_types=types.ContentType.ANY)
async def maker_message(message: types.Message):
    try:
        try:
            if message.photo[-1].file_id:
                photo = message.photo[-1].file_id
                caption = message.caption
                await message.answer_photo(photo=photo, caption=caption, reply_markup=confirmation_send_button)
                await Admin_all_user.confirmation_message.set()
                await message.delete()

        except:
            if message.video.file_id:
                video = message.video.file_id
                caption = message.caption
                await message.answer_video(video=video, caption=caption, reply_markup=confirmation_send_button)
                await Admin_all_user.confirmation_message.set()
                await message.delete()
    except:
        if not message.photo and not message.video:
            message_ = message.text
            await message.answer(message_, reply_markup=confirmation_send_button)
            await Admin_all_user.confirmation_message.set()
            await message.delete()


@dp.callback_query_handler(text="con:send", state=Admin_all_user.confirmation_message)
async def send_message(call: types.CallbackQuery):
    message = call.message
    users = db1.select_all_student()
    try:
        try:
            if message.photo[-1].file_id:
                for user in users:
                    photo = message.photo[-1].file_id
                    caption = message.caption
                    await bot.send_photo(chat_id=user[0], photo=photo, caption=caption)
                await call.answer("✅ Xabar hamma o'quvchiga jo'natildi", show_alert=True)
                await call.message.answer(f"Tugmalardan birini tanlang👇", reply_markup=admin_menu)
                await call.message.delete()
        except:
            if message.video.file_id:
                for user in users:
                    video = message.video.file_id
                    caption = message.caption
                    await bot.send_video(chat_id=user[0], video=video, caption=caption,
                                         reply_markup=confirmation_send_button)
                await call.answer("✅ Xabar hamma o'quvchiga jo'natildi", show_alert=True)
                await call.message.answer(f"Tugmalardan birini tanlang👇", reply_markup=admin_menu)
                await call.message.delete()

    except:
        if not message.photo and not message.video:
            for user in users:
                message_ = message.text
                await bot.send_message(chat_id=user[0], text=message_)
            await call.answer("✅ Xabar hamma o'quvchiga jo'natildi", show_alert=True)
            await call.message.answer(f"Tugmalardan birini tanlang👇", reply_markup=admin_menu)
            await call.message.delete()