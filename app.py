from aiogram import executor

from loader import dp, db, db1
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

try:
    db.create_table_circle()
except Exception as err:
    print(err)

try:
    db1.create_table_student_info()
except Exception as err:
    print(err)


async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)


