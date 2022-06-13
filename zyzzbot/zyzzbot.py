#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .msgman import MsgMan


class ZyzzBot(MsgMan):
    """Bot commands management."""

    def calculate(self, update, context):
        self.chat_id = update.effective_chat["id"]

        self.set_update(update)
        self.clean_start()
        self.set_context(context)

        data = self.db.get_last_record(self.get_user())
        if data is not None:
            self.data = data

        self.set_status("data: showing")

        img = self.make_img()
        msg = self.make_msg()
        keyboard = self.make_keyboard()

        self.send(img, msg, keyboard)

    def motivate(self, update, context):
        pass

    def info(self, update, context):
        self.chat_id = update.effective_chat["id"]

        self.set_update(update)
        self.clean_start()
        self.set_context(context)

        self.set_status("informing")

        img = self.make_img()
        msg = """Q: Why do I graph the scores and not the fat% and ffmi?
A: It's easier to graph and to understand.
   Anyway, I'm working at more graphs styles.

Q: How the scores are calculated?
A: For males I take 50 as the mean of the population values and 100 as 8% of fat% and 25 of ffmi.
   For females the formula give me errors, so I disable it, I'm sorry :(

Q: Does it mean I should point to get 100?
A: No way, the score is just a reference,
   it's usefull to know where the natural limits are to set a goal,
   but this is an individual journey, don't compare to others,
   we all gonna make it brah!

Please if you have more questions, contact @Seburath,
He will be glad to talk to you to make me better ZyzzBot.
        """

        keyboard = self.get_keyboard("delete: confirm")

        self.send(img, msg, keyboard)

    def reminderon(self, update, context):
        pass

    def reminderoff(self, update, context):
        pass

    def deletelastentry(self, update, context):
        self.set_update(update)
        self.clean_start()
        self.set_status("deletelastdatapoint: comfirming")

        self.data = self.db.get_last_record("Seburath")

        img = self.make_img()
        msg = "Do you want me to delete the last datapoint?"
        keyboard = self.get_keyboard("delete: confirm")

        self.send(img, msg, keyboard)

    def deleteallmydata(self, update, context):
        self.set_update(update)
        self.clean_start()
        self.set_status("deletealldata: comfirming")

        self.data = self.db.get_last_record("Seburath")

        img = self.make_img()
        msg = "Do you want me to delete all your data?"
        keyboard = self.get_keyboard("delete: confirm")

        self.send(img, msg, keyboard)

    def handle_text(self, update, context):
        self.set_context(context)
        self.set_update(update)

        text = update.message.text
        self.process_text(text)

    def handle_button(self, update, context):
        self.set_context(context)
        self.set_update(update)
        self.set_query(update)

        self.query.answer()

        button = self.query.data
        self.process_button(button)

    def log_errors(self, update, context):
        """Log Errors caused by Updates."""
        self.log('Update "%s" caused error "%s"', update, context.error)
