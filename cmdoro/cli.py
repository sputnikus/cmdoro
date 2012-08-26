# -*- coding: utf-8 -*-
"""
    cmdoro.cli
    ~~~~~~~~~~

    Countdown CLI in curses (with some colors and stuff)

    :copyright: (c) 2012 by Martin Putniorz.
    :license: BSD, see LICENSE for details.
"""
import sys

import urwid

from config import loader


class CmdoroWidget(urwid.Text):
    """CMDoro timer widget"""

    _selectable = True
    signals = ['started', 'switch']

    def __init__(self, *args, **kwargs):
        config_dict = loader()
        self.work_time = config_dict['work_time']
        self.rest_time = config_dict['rest_time']

        self.started = False
        self.time = self.work_time
        self._context = 'work'
        super(CmdoroWidget, self).__init__('CMDoro version 0.1. Press spacebar \
and get shit done.')

    def update(self):
        if self.started:
            if self._context == 'work':
                self.set_text('Working now. Remaining time: %d minutes'\
                    % self.time)
            else:
                self.set_text('Resting now. Remaining time: %d minutes'\
                    % self.time)
        self.time -= 1
        if self.time:
            return True
        else:
            self._emit('switch')

    def start(self):
        self.started = True
        self._emit('started')

    def keypress(self, size, key):
        if key == ' ':
            self.start()
        else:
            return key
        if not self.started:
            self.set_text('Neco')

    def get_context(self):
        return self._context

    def set_context(self, new_context):
        if new_context in ('work', 'rest'):
            self._context = new_context
            if new_context == 'work':
                self.time = self.work_time
            else:
                self.time = self.rest_time
        self._emit('started')

    context = property(get_context, set_context)


def unhandled_input(key_input):
    """Exits cmdoro if Q/q or escape is catched

    :param key_input: Key pressed"""
    if key_input in ('q', 'Q', 'esc'):
        raise urwid.ExitMainLoop()


def update_timer(loop, cmdoro):
    if not cmdoro.started:
        return
    if cmdoro.update():
        loop.set_alarm_in(60, update_timer, cmdoro)


def switch_update_timer(cmdoro, loop):
    update_timer(loop, cmdoro)


def switch_context(cmdoro):
    cmdoro.context = 'rest' if cmdoro.context == 'work' else 'work'


def main():
    """Main urwid loop"""
    try:
        cmdoro = CmdoroWidget()
    except IOError:
        text = urwid.Text('CMDoro: Invalid config file!')
        filler = urwid.Filler(text, 'top')
        loop = urwid.MainLoop(filler, unhandled_input=unhandled_input)
        loop.run()
        sys.exit(1)

    cmdoro_fill = urwid.Filler(cmdoro, 'top')

    loop = urwid.MainLoop(cmdoro_fill, unhandled_input=unhandled_input)
    urwid.connect_signal(cmdoro, 'started', switch_update_timer, loop)
    urwid.connect_signal(cmdoro, 'switch', switch_context)
    loop.run()
