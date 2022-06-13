#!/usr/bin/env python3
#

import datetime as dt


def is_fd():
    return False


def get_price(cmd):
    if cmd == "Estiba":
        price = 0.05

        if is_fd():
            price += 0.02

    else:
        price = 0.1

    return price
