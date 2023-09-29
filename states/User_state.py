from aiogram.dispatcher.filters.state import State, StatesGroup


class user_state(StatesGroup):
    week_search = State()
    science = State()
