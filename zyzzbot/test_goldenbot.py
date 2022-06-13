#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase
from telegram import Update

from .db import DBMan
from .goldenbot import GoldenBot
from .picky import Picky


class TestGoldenbot(TestCase):
    chat_id = -776891381
    token = "5223922019:AAHOdMdzuPHwN9ZH_Xm5ZdWz69UuccwXfyc"
    db = DBMan("Test")

    bot = GoldenBot(chat_id, token, db)
    dp = bot.updater.dispatcher

    def test_inventario(self):
        obj = Picky.load("update_inventario_empty")
        update = Update.de_json(obj, self.bot)
        assert self.bot.in_goldenchat(update) is True

        self.bot.clean_start()

        self.bot.set_update(update)
        assert self.bot.update == update

        msg = self.bot.get_inventario()
        assert msg == ""

    def test_reset(self):
        obj = Picky.load("update_inventario_empty")
        update = Update.de_json(obj, self.bot)
        assert self.bot.in_goldenchat(update) is True

        self.bot.clean_start()

        self.bot.set_update(update)
        assert self.bot.update == update

        self.bot.set_status("reset: showing")
        assert self.bot.status == "reset: showing"
