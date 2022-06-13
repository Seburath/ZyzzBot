#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Keyboards used by GoldenBot
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from .emoji_remover import remove_emojis


def make_button(layout, callback=None):
    callback = remove_emojis(layout) if callback is None else callback

    if ":" in callback:
        callback = callback.split(":")[0]

    return InlineKeyboardButton(layout, callback_data=callback)


def make_buttons(layouts):
    buttons = []
    for layout in layouts:
        buttons.append(make_button(layout))

    return buttons


def ddata(data):
    buttons = []
    row = []

    buttons = [
        make_buttons(
            [
                f"gender: {data['gender']}",
                f"weight: {data['weight']}kg",
            ]
        ),
        make_buttons(
            [
                f"height: {data['height']}cm",
                f"neck: {data['neck']}cm",
            ]
        ),
        make_buttons(
            [
                f"waist: {data['waist']}cm",
                # f"hip: {data['hip']}cm",
            ]
        ),
        # make_buttons(["🔼Save", "❌MOTIVATE ME!❌"]),
    ]

    return InlineKeyboardMarkup(buttons)


def confirm(db):
    buttons = [
        make_buttons(["✅Yes", "❎No"]),
        make_buttons(["❌Cancel"]),
    ]

    return InlineKeyboardMarkup(buttons)


def no_keyboard_found(db):
    buttons = []
    buttons.append(make_buttons(["NoKeyboardFound"]))

    return InlineKeyboardMarkup(buttons)


class Keyboards:
    def __init__(self, db):
        self.db = db

    def gen_keyboard(self, keyboard):
        """Keyboards generator for TelMan"""

        if keyboard == "delete: confirm":
            return confirm

        return no_keyboard_found

    def get_keyboard(self, keyboard):
        keyboard_generator = self.gen_keyboard(keyboard)

        return keyboard_generator(self.db)

    def get_keyboard_from_dict(self, data):
        return ddata(data)
