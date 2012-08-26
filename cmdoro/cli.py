# -*- coding: utf-8 -*-
"""
    cmdoro.cli
    ~~~~~~~~~~

    Countdown CLI in curses (with some colors and stuff)

    :copyright: (c) 2012 by Martin Putniorz.
    :license: BSD, see LICENSE for details.
"""
import sys
import time

import urwid

from config import loader
from signals import MinuteSig, DoneSig


def countdown(minutes):
    """The countdown generator, yields on minute change

    :param minutes: Countdown time in minutes
    """

    for minute in range(minutes, 0, -1):
        yield minutes
        time.sleep(60)


def main():
    """Main screen of cmdoro"""
    try:
        config_dict = loader()
    except IOError:
        text = urwid.Text('CMDoro: Invalid config file!')
        filler = urwid.Filler(text, 'top')
        loop = urwid.MainLoop(filler, unhandled_input=unhandled_input)
        loop.run()
        sys.exit(1)

    text = urwid.Text('CMDoro version 0.1')
    filler = urwid.Filler(text, 'top')
    loop = urwid.MainLoop(filler, unhandled_input=unhandled_input)
    loop.run()


def unhandled_input(key_input):
    """Exits cmdoro if Q/q or escape is catched

    :param key_input: Key pressed"""
    if key_input in ('q', 'Q', 'esc'):
        raise urwid.ExitMainLoop()


def working():
    """Working stage countdown"""
    pass


def resting():
    """Resting stage countdown"""
    pass
