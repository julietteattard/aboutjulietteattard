set -ex
IMAGETOBOOT=~/debiantesting.qcow2
IMAGETOINSTALL=~/debian-testing-amd64-DVD-1.iso
file $IMAGETOBOOT | grep 'QEMU QCOW Image' || ( echo 'not real boot img' && exit 2 ) 
qemu-system-x86_64 -accel kvm -cpu host,migratable=off -M pc -smp 6 -m 20G \
-drive file="$IMAGETOINSTALL",index=1,media=cdrom \
-drive file="$IMAGETOBOOT",driver=qcow2,media=disk,discard=on,if=virtio
qemu-img convert -O qcow2 "$IMAGETOBOOT" "$IMAGETOBOOT".shrunk.qcow2 && mv "$IMAGETOBOOT".shrunk.qcow2 "$IMAGETOBOOT"

