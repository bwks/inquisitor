import logging

from inquisitor.constants import TEMPLATE_SEARCH_PATH
from inquisitor.loaders import load_template
from inquisitor.translators import textfsm_to_dict

logger = logging.getLogger(__name__)


def data_dict(data_type, raw_data, template):

    texfsm_template = ''
    for path in TEMPLATE_SEARCH_PATH:
        try:
            texfsm_template = load_template(template, path)
        except FileNotFoundError:
            logger.info(f'File not found: {path}/{template}')

    if not texfsm_template:
        raise FileNotFoundError(f'Template file "{template}" not found')

    return textfsm_to_dict(texfsm_template, data_type, raw_data)
