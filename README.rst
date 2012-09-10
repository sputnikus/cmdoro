.. -*-restructuredtext-*-
CMDoro: Pomodoro for your shell
===============================

CMDoro is dead simple Pomodoro timer for your shell. Currently is completely untested, in some kind of alpha stage (doesn't even has setup.py and stuff)


How to get it running
---------------------
* Install requirements ::

    $ pip install -r requirements.txt

* Write your configuration file (in ``YAML`` format) ::

    ---
    work_time: <your work time in minutes>
    rest_time: <your rest time in minutes>
    ...

* Export environment varible ``CMDORO_CONFIG`` with path to your configuration
* Run it! ::

    $ ./run


TODO
----
* More options
* Plugin system
* Tests