from aiogram import types
from aiogram.dispatcher import FSMContext


from keyboards.default.search_button import search_button_user
from keyboards.inline.admin_weekdays import week_days2
from keyboards.inline.science_name_inline import science
from loader import dp
from states.User_state import user_state


@dp.callback_query_handler(text="week:back", state=user_state.week_search)
@dp.callback_query_handler(text="science:back", state=user_state.science)
async def sub_back(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Qidirish turini tanlang 🤳", reply_markup=search_button_user)
    await state.finish()
    await call.message.delete()


@dp.message_handler(text="🔙 Ortga", state=user_state.week_search)
async def week_search_back(message: types.Message):
    await message.answer('📆 Hafta kunini tanlang', reply_markup=week_days2)
    await user_state.week_search.set()
    await message.delete()


@dp.message_handler(text="🔙 Ortga", state=user_state.science)
async def sub_search_back(message: types.Message):
    await message.answer("To'garak fanini tanlang 👇", reply_markup=science)
    await user_state.science.set()
    await message.delete()


@dp.message_handler(text="🔝 Bosh Menyu", state=user_state.science)
@dp.message_handler(text="🔝 Bosh Menyu", state=user_state.week_search)
async def menu_back(message: types.Message, state: FSMContext):
    await message.answer("Qidirish turini tanlang 🤳", reply_markup=search_button_user)
    await state.finish()
    await message.delete()

