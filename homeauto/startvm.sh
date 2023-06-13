#!/usr/bin/env bash
# This file is part of aboutjulietteattard
# Copyright (C) 2023 Juliette Attard
set -ex
IMAGETOBOOT=~/debiantesting.qcow2
IMAGETOINSTALL=~/debian-testing-amd64-DVD-1.iso
BRIDGENAME=qemumacvtap0
file $IMAGETOBOOT | grep 'QEMU QCOW Image' || ( echo 'not real boot img' && exit 2 ) 
qemu-system-x86_64 -accel kvm -cpu host,migratable=off -M pc -smp 6 -m 20G \
-drive file="$IMAGETOINSTALL",index=1,media=cdrom \
-drive file="$IMAGETOBOOT",driver=qcow2,media=disk,discard=on,if=virtio \
-net nic,model=virtio,macaddr=$(cat /sys/class/net/$BRIDGENAME/address) \
-net tap,fd=3 3<>/dev/tap$(cat /sys/class/net/$BRIDGENAME/ifindex)
# -netdev tap,id=tap1,ifname="$BRIDGENAME",script=no,downscript=no -device virtio-net,netdev=tap1

qemu-img convert -O qcow2 "$IMAGETOBOOT" "$IMAGETOBOOT".shrunk.qcow2 && mv "$IMAGETOBOOT".shrunk.qcow2 "$IMAGETOBOOT"

