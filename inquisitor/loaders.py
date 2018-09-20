import os
import json

import textfsm

from .constants import TEXTFSM_TEMPLATES_DIR


def load_template(template, location=TEXTFSM_TEMPLATES_DIR):
    try:
        with open(f'{location}/{template}', 'r') as f:
            return textfsm.TextFSM(f)
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found: {location}/{template}')


def load_config(location='~/.config'):
    try:
        with open(os.path.expanduser(location), 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        config = {}
    return config


def load_host_data(filename='hosts.txt', location='./'):
    try:
        with open(f'{location}/{filename}', 'r') as f:
            return [i.strip() for i in f.readlines()]
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found: {location}/{filename}')
