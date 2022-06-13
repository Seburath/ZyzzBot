#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

import matplotlib.pyplot as plt
import matplotlib as mpl

from telegram.ext import Updater

from .calculator import Calculator
from .keyboards import Keyboards


class TelMan:
    """Telegram manager for GoldenBot."""

    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    log = logging.getLogger(__name__).info
    separator = "---------------------------------\n"

    def __init__(self, chat_id, token, db):
        self.db = db
        self.chat_id = chat_id

        self.status = ""
        self.updater = Updater(token, use_context=True)

        self.keyboards = Keyboards(db)
        self.get_keyboard = self.keyboards.get_keyboard

    def set_chat_id(self):
        pass

    def recalculate(self):
        gender = self.data["gender"]
        neck = self.data["neck"]
        height = self.data["height"]
        weight = self.data["weight"]
        waist = self.data["waist"]
        hip = self.data["hip"]

        try:
            body_fat = Calculator.get_fat_percentage(
                height, neck, waist, gender="m", hip=0
            )
            fat_score = int(Calculator.get_fat_score(body_fat, gender="m"))

            ffmi = Calculator.get_ffmi(height, weight, body_fat)
            muscle_score = int(Calculator.get_ffmi_score(ffmi, gender="m"))

            total_score = (fat_score + muscle_score) // 2

            self.data["body_fat"] = body_fat
            self.data["fat_score"] = fat_score

            self.data["ffmi"] = ffmi
            self.data["muscle_score"] = muscle_score

            self.data["total_score"] = total_score

            return 0

        except:
            return 1

    def make_msg(self):
        body_fat = str(round(self.data["body_fat"], 2))
        fat_score = str(int(self.data["fat_score"]))

        ffmi = str(round(self.data["ffmi"], 2))
        muscle_score = str(int(self.data["muscle_score"]))

        total_score = str(int(self.data["total_score"]))

        msg = [
            f"Body Fat %: {body_fat}\n",
            f"FFMI: {ffmi}\n",
            f"Fat Score: {fat_score}\n",
            f"Muscle Score: {muscle_score}\n",
            f"Total: {total_score}\n",
        ]

        return " ".join(msg)

    def make_keyboard(self):
        return self.keyboards.get_keyboard_from_dict(self.data)

    def make_img(self):
        datapoints = self.db.get_datapoints(self.get_user())

        COLOR = "gray"
        mpl.rcParams["text.color"] = COLOR
        mpl.rcParams["axes.labelcolor"] = COLOR
        mpl.rcParams["xtick.color"] = COLOR
        mpl.rcParams["ytick.color"] = COLOR

        plt.xlabel("Date")
        x = datapoints["date"]

        plt.ylabel("Score")
        y = datapoints["fat_score"]
        plt.plot(x, y, label="fat_score", linewidth=2, color="grey", marker="o")

        y = datapoints["muscle_score"]
        plt.plot(x, y, label="muscle_score", linewidth=2, color="red", marker="o")

        plt.legend()
        plt.tight_layout()
        plt.grid()
        plt.savefig("f.png", facecolor="black", transparent=True)
        plt.clf()

        return open("f.png", "rb")

    def clean_start(self):
        self.set_status("")
        self.cmd = ""
        self.data = {
            "user": self.get_user(),
            "gender": "M",
            "height": 171,
            "neck": 42,
            "waist": 85,
            "hip": 0,
            "weight": 75,
            "body_fat": 0,
            "fat_score": 0,
            "ffmi": 0,
            "muscle_score": 0,
            "total_score": 0,
        }

    def set_update(self, update):
        self.update = update

    def set_context(self, context):
        self.context = context

    def set_query(self, update):
        self.query = update.callback_query

    def set_status(self, status):
        self.log(status)
        self.status = status

    def gen_keyboard(self, status):
        return self.keyboards.get_keyboard(status)

    def send(self, img, msg, keyboard):
        self.context.bot.sendPhoto(
            chat_id=self.chat_id,
            photo=img,
            caption=msg,
            reply_markup=keyboard,
        )

    def edit(self, msg, keyboard=None):
        self.context.bot.editMessageCaption(
            chat_id=self.chat_id,
            message_id=self.query.message.message_id,
            caption=msg,
        )

    def erase_msg(self, msg_id):
        self.updater.bot.delete_message(self.chat_id, msg_id)

    def erase_updated_message(self):
        self.erase_msg(self.update.message.message_id)

    def get_user(self):
        return self.update.message.from_user.username
