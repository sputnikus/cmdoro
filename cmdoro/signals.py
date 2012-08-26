# -*- coding: utf-8 -*-
"""
    cmdoro.signals
    ~~~~~~~~~~~~~~

    Custom urwid signals

    :copyright: (c) 2012 by Martin Putniorz.
    :license: BSD, see LICENSE for details.
"""
import urwid


class MinuteSig(object):
    """Minute change signal"""
    __metaclass__ = urwid.signals.MetaSignals
    signals = ['minute']

    def send_signal(self):
        urwid.emit_signal(self, 'minute')


class DoneSig(object):
    """Done signal"""
    __metaclass__ = urwid.signals.MetaSignals
    signals = ['done']

    def send_signal(self):
        urwid.emit_signal(self, 'done')
