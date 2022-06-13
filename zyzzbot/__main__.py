#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ERP bot from Goldencalizas.
"""

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
)

from .db import DBMan
from .zyzzbot import ZyzzBot


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary

    chat_id = 00000000
    token = ""
    db = DBMan("PGContainer")

    bot = ZyzzBot(chat_id, token, db)
    dp = bot.updater.dispatcher

    dp.add_handler(CommandHandler("start", bot.calculate))
    dp.add_handler(CommandHandler("calculate", bot.calculate))

    dp.add_handler(CommandHandler("motivateme", bot.motivate))

    dp.add_handler(CommandHandler("info", bot.info))

    dp.add_handler(CommandHandler("reminderon", bot.reminderon))
    dp.add_handler(CommandHandler("reminderoff", bot.reminderoff))

    dp.add_handler(CommandHandler("deletelastentry", bot.deletelastentry))
    dp.add_handler(CommandHandler("deleteallmydata", bot.deleteallmydata))

    dp.add_handler(MessageHandler(Filters.text, bot.handle_text))
    dp.add_handler(CallbackQueryHandler(bot.handle_button))
    dp.add_error_handler(bot.log_errors)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    bot.updater.start_polling()
    bot.updater.idle()


if __name__ == "__main__":
    main()
