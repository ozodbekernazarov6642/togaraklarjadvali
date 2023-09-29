import datetime

from aiogram.dispatcher.filters.state import State, StatesGroup


class Admin_state(StatesGroup):
    add_week_day = State()
    choose_subject = State()
    circle_name = State()
    teacher_name = State()
    start_time = State()
    finish_time = State()
    confirmation = State()


class Admin_search(StatesGroup):
    menu_search = State()
    week_search = State()
    subject_search = State()


class Admin_delete(StatesGroup):
    circle_delete = State()
    delete_confirmation = State()


class Admin_all_user(StatesGroup):
    input_message = State()
    confirmation_message = State()



