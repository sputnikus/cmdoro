# -*- coding: utf-8 -*-
"""
    cmdoro.timer
    ~~~~~~~~~~~~

    Timer functions (for final countdown)

    :copyright: (c) 2012 by Martin Putniorz.
    :license: BSD, see LICENSE for details.
"""
import time


def countdown(seconds):
    """The countdown generator, yields on minute change

    :param seconds: Countdown time in seconds
    """
    trail = seconds % 60

    # trailing seconds, we want to count by a minute
    time.sleep(trail)
    seconds -= trail
    yield (seconds / 60)

    while seconds > 0:
        # now yield each minute
        time.sleep(60)
        seconds -= 60
        yield (seconds / 60)
