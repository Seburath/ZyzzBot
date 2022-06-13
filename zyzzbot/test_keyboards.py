#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from .keyboards import Keyboards
from .db import DBMan


class TestKeyboards(TestCase):
    db = DBMan("Test")
    keyboards = Keyboards(db)

    def test_trabajadores(self):
        self.assertEqual(
            str(type(self.keyboards.get_keyboard("trabajadores"))),
            "<class 'telegram.inline.inlinekeyboardmarkup.InlineKeyboardMarkup'>",
        )

    def test_unexistent_keyboard(self):
        self.assertEqual(
            str(type(self.keyboards.get_keyboard(None))),
            "<class 'telegram.inline.inlinekeyboardmarkup.InlineKeyboardMarkup'>",
        )
        self.assertEqual(
            str(type(self.keyboards.get_keyboard("unexistent_keyboard"))),
            "<class 'telegram.inline.inlinekeyboardmarkup.InlineKeyboardMarkup'>",
        )
