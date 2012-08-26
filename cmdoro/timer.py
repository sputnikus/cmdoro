# -*- coding: utf-8 -*-
"""
    cmdoro.timer
    ~~~~~~~~~~~~

    Timer functions (for final countdown)

    :copyright: (c) 2012 by Martin Putniorz.
    :license: BSD, see LICENSE for details.
"""
import time


def countdown(minutes):
    """The countdown generator, yields on minute change

    :param minutes: Countdown time in minutes
    """

    for minute in range(minutes, 0, -1):
        yield minutes
        time.sleep(60)
