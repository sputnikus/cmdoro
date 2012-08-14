# -*- coding: utf-8 -*-
"""
    cmdoro.config
    ~~~~~~~~~~~~~

    Config management

    :copyright: (c) 2012 by Martin Putniorz.
    :license: BSD, see LICENSE for details.
"""
import os
import sys

import yaml

# Currently considered cmdoro options
VALID_OPTIONS = ('work_time', 'rest_time')


def loader():
    """Loads YAML config from path specified in enviroment variable"""
    path = os.getenv('CMDORO_CONFIG')
    # If config file is not specified, get one from home directory
    if path is None:
        path = os.path.join(os.getenv('HOME'), 'cmdoro.yaml')

    with file(path) as config_file:
        config_dict = yaml.load(config_file)

    try:
        validate_config(config_dict)
    except KeyError, e:
        print e
        sys.exit(1)

    return config_dict


def validate_config(configs):
    for key in VALID_OPTIONS:
        if key not in configs:
            raise KeyError('You need to specify %s value in your config!'
                % key)
