#!/usr/bin/env python3
# This file is part of aboutjulietteattard
# Copyright (C) 2023 Juliette Attard
HEADER_TEXT='''# This file is part of aboutjulietteattard
# Copyright (C) 2023 Juliette Attard
'''
import subprocess
import json
import os
import shutil


NETDEV_HYPERVISOR_NET='''[NetDev]
Name={createname}
Kind=macvlan
[MACVLAN]
Mode=private
'''

NETWORK_BIND_WIRED='''[Match]
Name={wiredname}
[Network]
DHCP=false
'''
BIND_VTAP_TO_WIRED_ENTRY = 'MACVTAP={createname}'

NETWORK_BIND_WIRELESS='''[Match]
Name={wirelessname}
[Network]
DHCP=true
'''

DEV_OUTPUT= \
'''
{ifname}    {operstate}
    virtnet_type:{virtnet_type}
    addresses: {address}/{ipv4}/{ipv6}
'''

GET_IP_ARGV = ('ip', '-json', '-d', 'a')
WLAN_ADP_NAME = 'wlp8s0'
PHYS_INTFS = (WLAN_ADP_NAME, 'eno1')
def normalize_ip_device(ip_device_data):
    data = {'ifname':ip_device_data['ifname'],
    'address':ip_device_data['address'],
    'operstate':ip_device_data['operstate'],
    }
    ipv4='ipv4 unset'
    ipv6='ipv6 unset'
    if not ip_device_data.get('linkinfo'):
        virtnet_type='realdev'
    else:
        virtnet_type=ip_device_data['linkinfo']['info_kind']
        virtnet_type+='/'+ip_device_data['linkinfo']['info_data'].get('mode',)
    data['virtnet_type'] = virtnet_type
    for addr_info in ip_device_data.get('addr_info'):
        if addr_info['family'] == 'inet':
            ipv4 = addr_info['local']
        if addr_info['family'] == 'inet6' and addr_info['scope'] != 'link':
            ipv6 = addr_info['local']
    data['ipv4'] = ipv4
    data['ipv6']=ipv6
    return data
    
def write_files(directory, vmcount):
    if os.path.isdir(directory):
        shutil.rmtree(directory)
    os.mkdir(directory)
    for i in range(1, vmcount+1):
        createname = f'qemumacvtap{i}'
        filename = f'01-{createname}.netdev'
        with open(os.path.join(directory, filename), 'w') as fd:
            fd.write(HEADER_TEXT)
            fd.write(NETDEV_HYPERVISOR_NET.format(createname=createname))
    with open(os.path.join(directory, '02-bind-wired.network'), 'w') as fd:
        fd.write(HEADER_TEXT)
        fd.write(NETWORK_BIND_WIRED.format(wired=wiredname))

def main():
    current_ipdata = json.loads(subprocess.check_output(GET_IP_ARGV, text=True))
    analyzed = [normalize_ip_device(x) for x in sorted(current_ipdata, key=lambda x: x['ifname'])]
    for x in analyzed:
        if x['ifname'] in PHYS_INTFS:
            print(DEV_OUTPUT.format(**x))
    write_files('generated', 2)
    
if __name__ == '__main__':
    main()
