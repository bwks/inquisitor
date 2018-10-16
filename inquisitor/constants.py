import os

BASE_DIR = os.path.join(os.path.dirname(__file__))
TEXTFSM_TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
NTC_TEMPLATES_DIR = './ntc-templates/templates'


CISCO_IOS_SHOW_IP_ARP_TEMPLATE = 'cisco_ios_show_ip_arp.template'
CISCO_IOS_SHOW_IP_ROUTE_TEMPLATE = 'cisco_ios_show_ip_route.template'
CISCO_IOS_DIR_TEMPLATE = 'cisco_ios_dir.template'
CISCO_IOS_SHOW_IP_PROTOCOLS_SUMMARY_TEMPLATE = 'cisco_ios_show_ip_protocols_summary.template'
CISCO_IOS_SHOW_VRF_TEMPLATE = 'cisco_ios_show_vrf.template'
CISCO_IOS_SHOW_VERSION_TEMPLATE = 'cisco_ios_show_version.template'
CISCO_IOS_SHOW_INTERFACES_TEMPLATE = 'cisco_ios_show_interfaces.template'

TEMPLATE_SEARCH_PATH = [
    NTC_TEMPLATES_DIR,
    TEXTFSM_TEMPLATES_DIR,
    './templates'
]
