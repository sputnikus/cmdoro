# -*- coding: utf-8 -*-
"""
    cmdoro.cli
    ~~~~~~~~~~

    Countdown CLI in curses (with some colors and stuff)

    :copyright: (c) 2012 by Martin Putniorz.
    :license: BSD, see LICENSE for details.
"""
import curses
from timer import countdown
from config import loader


# Basic window color - white on black
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
# Working color - yellow on black
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
# Rest color - green on black
curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)


def main_screen(stdscr):
    """Main screen of cmdoro

    :param stdscr: Intialized curses screen
    """
    config_dict = loader()
    end = False

    try:
        while not end:
            working(stdscr, config_dict['work_time'])
            resting(stdscr, config_dict['rest_time'])


main = curses.wrapper(main_screen)


def working(stdscr, work_time):
    for minute in countdown(work_time):
        stdscr.addstr(0, 0, 'Working now. Remaining time: ', curses.color_pair(1))
        stdscr.addstr(0, 25, '%d minutes' % work_time, curses.color_pair(2))
        stdscr.refresh()


def resting(stdscr, rest_time):
    for minute in countdown(rest_time):
        stdscr.addstr(0, 0, 'Resting now. Remaining time: ', curses.color_pair(1))
        stdscr.addstr(0, 25, '%d minutes' % rest_time, curses.color_pair(3))
        stdscr.refresh()

    stdscr.addstr('Resting time\'s over! Want to contine? [A/n]')
    stdscr.refresh()
    choice = stdscr.getch()

    if choice not in (ord('n'), ord('N')):
        return True
    return False
