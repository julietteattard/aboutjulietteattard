#!/usr/bin/env bash
# This file is part of aboutjulietteattard
# Copyright (C) 2023 Juliette Attard
systemctl enable systemd-networkd
networkctl delete qemumacvtap0
echo '
ACTION=="add", SUBSYSTEM=="net", GROUP="netdev", MODE="0660"
ACTION=="add", SUBSYSTEM=="macvtap", GROUP="netdev", MODE="0660"
' > /etc/udev/rules.d/99-set_tun_netdev.rules
udevadm control -R
rm -f /etc/systemd/network/* 
cp *.network *.netdev /etc/systemd/network/ 
chown root:root /etc/systemd/network/*
systemctl restart systemd-networkd.service
sleep 1
ping 8.8.8.8 -c 1
journalctl -u systemd-networkd --since "30 seconds ago"
