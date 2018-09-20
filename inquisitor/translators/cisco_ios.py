from inquisitor.loaders import load_template
from inquisitor.constants import (
    cisco_ios_show_ip_arp_template,
    cisco_ios_show_ip_route_template,
    cisco_ios_dir_template,
    cisco_ios_show_ip_protocols_summary_template,
    cisco_ios_show_vrf_template,
    cisco_ios_show_version_template,
    cisco_ios_show_interfaces_template,
)


def show_ip_arp_to_dict(data):
    template = load_template(cisco_ios_show_ip_arp_template)
    arp_list = template.ParseText(data)

    arp_dict = {}
    for i in arp_list:
        arp_dict.update({
            i[0]: {
                'mac_address': i[2],
                'type': i[3],
                'interface': i[4]
            }
        })
    return arp_dict


def show_ip_route_static_to_dict(data):
    template = load_template(cisco_ios_show_ip_route_template)
    routes_list = template.ParseText(data)

    routes_dict = {'static_routes': []}
    for i in routes_list:
        if i[0] == 'S':
            routes_dict['static_routes'].append({
                'prefix': f'{i[2]}/{i[3]}',
                'next-hop': i[7],
                'metric': i[4],
            })
    return routes_dict


def dir_to_dict(data):
    template = load_template(cisco_ios_dir_template)
    files_list = template.ParseText(data)

    files_dict = {i[0]: [] for i in files_list}
    for i in files_list:
        files_dict[i[0]].append({
            'size': i[3],
            'filename': i[7],
        })
    return files_dict


def show_ip_protocols_summary_to_dict(data):
    template = load_template(cisco_ios_show_ip_protocols_summary_template)
    protocols_list = template.ParseText(data)

    protocols_dict = {}
    for i in protocols_list:
        protocols_dict.update({
            i[0]: i[1]
        })
    return protocols_dict


def show_vrf_to_dict(data):
    template = load_template(cisco_ios_show_vrf_template)
    vrf_list = template.ParseText(data)

    vrf_dict = {}
    for i in vrf_list:
        vrf_dict.update({
            i[0]: {
                'default_rd': i[1],
                'protocol': i[2],
                'interfaces': [y for y in i[3] if '' != y],
            }
        })
    return vrf_dict


def show_version_to_dict(data):
    """
    Convert a textfsm data structure to a dictionary
    :param data: textfsm data structure
      [['15.6(1)T', 'Bootstrap', 'iosv', '19 minutes', '/vios-adventerprisek9-m', [], ['9F5AD57IY1430DLTI5483'], '0x0']]
    :return: Dict of data
    """
    template = load_template(cisco_ios_show_version_template)
    version_list = template.ParseText(data)[0]

    return {
        'software_version': version_list[0],
        'boot_image': version_list[4],
        'device_model': version_list[5],
        'device_serial': version_list[6],
        'config_register': version_list[7],
    }


def show_interfaces_to_dict(data):
    """
    Convert a textfsm data structure to a dictionary
    :param data: textfsm data structure
      [['GigabitEthernet0/0', 'up', 'up', 'iGbE', '5254.0023.79f0', '5254.0023.79f0', 'vagrant-management', '192.168.121.221/24', '1500', 'Auto Duplex', 'Auto Speed', '1000000 Kbit', '10 usec', 'ARPA', 'fifo', '1000', '1000']]
    :return: Dict of data
    """

    template = load_template(cisco_ios_show_interfaces_template)
    interface_list = template.ParseText(data)

    interface_dict = {}
    for i in interface_list:
        interface_dict.update({
            i[0]: {
                'status': i[1],
                'description': i[6],
                'mac_address': i[4],
                'ipv4_address': i[7],
                'mtu': i[8],
                'duplex': i[9],
                'speed': i[10],
                'bandwidth': i[11],
                'delay': i[12],
            }
        })
    return interface_dict
