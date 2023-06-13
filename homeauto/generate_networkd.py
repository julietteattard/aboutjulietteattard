#!/usr/bin/env python3
# This file is part of aboutjulietteattard
# Copyright (C) 2023 Juliette Attard
import subprocess
import json

NETDEV_HYPERVISOR_NET='''[NetDev]
Name={createname}
Kind=macvlan
[MACVLAN]
Mode=passthru
'''
DEV_OUTPUT= \
'''
{ifname}    {operstate}
    virtnet_type:{virtnet_type}
    addresses: {address}/{ipv4}/{ipv6}
'''

GET_IP_ARGV = ('ip', '-json', '-d', 'a')
WLAN_ADP_NAME = 'wlp10s0'
PHYS_INTFS = (WLAN_ADP_NAME, 'eno1')
def format_dev(**kwargs):
    data = {'ifname':kwargs['ifname'],
    'address':kwargs['address'],
    'operstate':kwargs['operstate'],
    }
    ipv4='ipv4 unset'
    ipv6='ipv6 unset'
    if not kwargs.get('linkinfo'):
        virtnet_type='realdev'
    else:
        virtnet_type=kwargs['linkinfo']['info_kind']
        virtnet_type+='/'+kwargs['linkinfo']['info_data'].get('mode',)
    data['virtnet_type'] = virtnet_type
    for addr_info in kwargs.get('addr_info'):
        if addr_info['family'] == 'inet':
            ipv4 = addr_info['local']
        if addr_info['family'] == 'inet6' and addr_info['scope'] != 'link':
            ipv6 = addr_info['local']
    data['ipv4'] = ipv4
    data['ipv6']=ipv6
    print(DEV_OUTPUT.format(**data))
def main():
    current_ipdata = json.loads(subprocess.check_output(GET_IP_ARGV, text=True))
    for devdata in sorted(current_ipdata, key=lambda x: x['ifname']):
        if devdata.get('linkinfo') or devdata['ifname'] in PHYS_INTFS:
            format_dev(**devdata)
if __name__ == '__main__':
    main()
