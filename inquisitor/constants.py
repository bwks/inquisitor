import os

BASE_DIR = os.path.join(os.path.dirname(__file__))
INQUISITOR_TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
NTC_TEMPLATES_DIR = './ntc-templates/templates'

TEMPLATE_SEARCH_PATH = [
    NTC_TEMPLATES_DIR,
    INQUISITOR_TEMPLATES_DIR,
    './templates'
]

CISCO_IOS_TEMPLATE_MAP = {
    'interfaces': 'cisco_ios_show_interfaces.template',
    'directories': 'cisco_ios_dir.template',
    'arp_table': 'cisco_ios_show_ip_route.template',
    'ipv4_routes': 'cisco_ios_show_ip_route.template',
    'ipv4_protocols': 'cisco_ios_show_ip_protocols_summary.template',
    'vrfs': 'cisco_ios_show_vrf.template',
    'version': 'cisco_ios_show_version.template',
}
