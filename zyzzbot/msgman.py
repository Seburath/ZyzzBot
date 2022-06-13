#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .telman import TelMan
from datetime import date, datetime
from dateutil import parser


class MsgMan(TelMan):
    """Messages manager for Goldenbot."""

    def process_text(self, text):
        """Manage text inputs."""

        if self.status != "":
            self.erase_updated_message()

        if self.status == "data: receiving":
            if self.button != "gender" and text.isdigit():
                text = int(text)

            self.data[self.button] = text

            response = self.recalculate()
            if response != 0:
                return

            last_record = self.db.get_last_record("Seburath")

            if last_record is None:
                self.db.add_record(self.data)

            if last_record is not None:
                last_datapoint_date = parser.parse(last_record["date"]).date()

                if last_datapoint_date == datetime.today().date():
                    self.db.replace_last_record(self.data)

                elif last_datapoint_date != datetime.today().date():
                    self.db.add_record(self.data)

            datapoints = self.db.get_datapoints("Seburath")
            last_record = self.db.get_last_record("Seburath")

            self.erase_msg(self.query.message.message_id)
            self.set_status("data: showing")

            img = self.make_img()
            msg = self.make_msg()
            keyboard = self.make_keyboard()

            self.log(self.data)
            self.send(img, msg, keyboard)

    def process_button(self, button):
        """Response in the button callback."""

        if button in [
            "height",
            "neck",
            "waist",
            "hip",
            "weight",
        ]:

            self.button = button
            self.set_status("data: receiving")

            msg = f"What's your new {button}?"
            self.edit(msg)
