import textfsm

from .constants import TEXTFSM_TEMPLATES_DIR


def load_template(template, location=TEXTFSM_TEMPLATES_DIR):
    try:
        with open(f'{location}/{template}', 'r') as f:
            return textfsm.TextFSM(f)
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found: {location}/{template}')
