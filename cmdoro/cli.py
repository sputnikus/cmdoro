# -*- coding: utf-8 -*-
"""
    cmdoro.cli
    ~~~~~~~~~~

    Countdown CLI in curses (with some colors and stuff)

    :copyright: (c) 2012 by Martin Putniorz.
    :license: BSD, see LICENSE for details.
"""
import curses
import sys

from timer import countdown
from config import loader


def main(stdscr):
    """Main screen of cmdoro

    :param stdscr: Intialized curses screen
    """
    # Basic window color - white on black
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    # Working color - yellow on black
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    # Rest color - green on black
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    try:
        config_dict = loader()
    except IOError, e:
        stdscr.addstr(0, 0, 'Problem with config: %s' % e, curses.color_pair(1))
        stdscr.refresh()
        sys.exit(1)
    end = False

    while not end:
        working(stdscr, config_dict['work_time'])
        end = resting(stdscr, config_dict['rest_time'])


def working(stdscr, work_time):
    stdscr.clear()
    stdscr.addstr(0, 0, 'Working now. Remaining time: ', curses.color_pair(1))
    for minute in countdown(work_time):
        stdscr.addstr(0, 29, '%d minutes' % minute, curses.color_pair(2))
        stdscr.refresh()


def resting(stdscr, rest_time):
    stdscr.clear()
    stdscr.addstr(0, 0, 'Resting now. Remaining time: ', curses.color_pair(1))
    for minute in countdown(rest_time):
        stdscr.addstr(0, 29, '%d minutes' % minute, curses.color_pair(3))
        stdscr.refresh()

    stdscr.clear()
    stdscr.addstr('Resting time\'s over! Want to contine? [A/n] ')
    stdscr.refresh()
    choice = stdscr.getch()

    if choice not in (ord('n'), ord('N')):
        return False
    return True
