import os
import json

import textfsm

from .constants import TEXTFSM_TEMPLATES_DIR


def load_template(template, location=TEXTFSM_TEMPLATES_DIR):
    with open(f'{location}/{template}', 'r') as f:
        return textfsm.TextFSM(f)


def load_config(location='~/.config'):
    with open(os.path.expanduser(location), 'r') as f:
        config = json.load(f)
    return config
