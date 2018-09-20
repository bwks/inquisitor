import time
import json
import logging

from multiprocessing.pool import ThreadPool as Pool

from netconnect.cisco import CiscoDriver
from netconnect.helpers import clean_output

from .utils import jprint
from .command_sets import cisco_ios_data_commands
from .translators import (
    show_ip_arp_to_dict,
    show_ip_route_static_to_dict,
    dir_to_dict,
    show_ip_protocols_summary_to_dict,
    show_vrf_to_dict,
    show_version_to_dict,
    show_interfaces_to_dict,
)
from .loaders import load_config, load_host_data

logger = logging.getLogger(__name__)

hosts = load_host_data()[:1]

config = load_config()
all_host_data = {}


def worker(host, command_set):
    time_now = time.time()
    raw_command_results = []

    with CiscoDriver(host, config['username'], config['password'],
                     disable_host_key_checking=True) as dev:
        result = dev.send_commands(command_set)
        raw_command_results = raw_command_results + result

        host_data = {}
        host_data['time_stamp'] = time_now
        host_data['interfaces'] = show_interfaces_to_dict(result[1])
        host_data.update(show_version_to_dict(result[0]))
        host_data['ipv4_protocols'] = show_ip_protocols_summary_to_dict(result[3])
        host_data['storage_volumes'] = dir_to_dict(result[4])
        host_data['routes'] = show_ip_route_static_to_dict(result[5])
        host_data['arp_table'] = show_ip_arp_to_dict(result[6])

        vrf_dict = show_vrf_to_dict(result[2])
        host_data['vrfs'] = vrf_dict

        for vrf in vrf_dict.keys():
            vrf_cmd = [f'show ip protocols vrf {vrf} summary']
            vrf_result = dev.send_commands(vrf_cmd)
            raw_command_results = raw_command_results + vrf_result

            host_data['vrfs'][vrf]['ipv4_protocols'] = show_ip_protocols_summary_to_dict(vrf_result[0])

        for vrf in vrf_dict.keys():
            vrf_cmd = [f'show ip arp vrf {vrf}']
            vrf_result = dev.send_commands(vrf_cmd)
            raw_command_results = raw_command_results + vrf_result

            host_data['vrfs'][vrf]['arp_table'] = show_ip_arp_to_dict(vrf_result[0])

    file_time = time.strftime("%Y-%m-%d--%H-%M-%S", time.localtime(time_now))
    with open(f'outputs/{host}-{file_time}-raw.txt', 'w') as f:
        for i in raw_command_results:
            f.write(clean_output(i, highlight_command=True))

    all_host_data[host] = host_data


def runner(hosts, pool_size=15):
    pool = Pool(pool_size)
    for host in hosts:
        pool.apply_async(worker, (host, cisco_ios_data_commands))
    pool.close()
    pool.join()


if __name__ == '__main__':
    start = time.time()
    runner(hosts, 150)
    end = time.time()
    jprint(all_host_data)
    print(end - start)
    print(len(hosts))

    for k, v in all_host_data.items():
        print(k, v['boot_image'])

    with open('host_data.json', 'w') as f:
        json.dump(all_host_data, f)
