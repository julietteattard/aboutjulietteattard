#!/usr/bin/env bash
# This file is part of aboutjulietteattard
# Copyright (C) 2023 Juliette Attard
rm -f /etc/systemd/network/* 
cp *.network *.netdevs /etc/systemd/network/ 
systemctl restart systemd-networkd -o verbose 
systemctl status systemd-networkd --no-pager -l
