import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.admin_button import admin_menu
from keyboards.default.back_button import back
from keyboards.inline.Confirmation import confirmation_button, confirmation_button2
from states.Admin_state import Admin_state, Admin_delete

from loader import dp, db
from data import config

code = {}


@dp.message_handler(text="🗑 To'garakni o'chirish", user_id=config.ADMINS)
async def delete(message: types.Message):
    await message.answer("🗑 O'chirish ko'dini kiriting", reply_markup=back)
    await Admin_delete.circle_delete.set()
    await message.delete()


@dp.message_handler(state=Admin_delete.circle_delete, user_id=config.ADMINS)
async def delete_circle(message: types.Message):
    global code
    circles = db.select_all_circle()
    id_ = message.text
    status = None
    try:
        if int(message.text):
            for circle in circles:
                if int(circle[0]) == int(id_):
                    response = (f"🔰 To'garak nomi: {circle[2]}\n\n"
                                f"📚 To'garak fani: {circle[3]}\n\n"
                                f"👨‍🏫 To'garak o'qituvchisi: {circle[4]}\n\n"
                                f"🗓 To'garak kunlari: {circle[1]}\n\n"
                                f"🕐 To'garak boshlanish vaqti: {circle[5]}\n\n"
                                f"🕠 To'garak tugash vaqti: {circle[6]}\n\n")
                    status = True
                    code['id'] = message.text
                    await message.answer(response, reply_markup=confirmation_button2)
                    await Admin_delete.delete_confirmation.set()
            if status != True:
                await message.answer("❌ O'chirish ko'di noto'g'ri")
    except:
        await message.answer("❌ O'chirish ko'dini to'g'ri kiriting")


@dp.callback_query_handler(text="con:delete", state=Admin_delete.delete_confirmation, user_id=config.ADMINS)
async def delete_(call: types.CallbackQuery, state: FSMContext):
    global code
    db.delete_circle_by_id(int(code["id"]))
    await call.answer("🗑 To'garak muvaffaqiyatli o'chirildi")
    await call.message.delete()
    await call.message.answer(f"Tugmalardan birini tanlang👇", reply_markup=admin_menu)
    await call.message.delete()
    await state.finish()
