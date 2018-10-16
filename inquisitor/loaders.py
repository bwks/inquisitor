import textfsm


def load_template(template, location='./'):
    try:
        with open(f'{location}/{template}', 'r') as f:
            return textfsm.TextFSM(f)
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found: {location}/{template}')
