import logging

from aiogram import Dispatcher

from configuration_data.config import admins


async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, "work")

        except Exception as err:
            logging.exception(err)