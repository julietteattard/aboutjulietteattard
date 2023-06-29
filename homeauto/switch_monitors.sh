#!/bin/bash
#!/usr/bin/env -S pkexec --keep-cwd bash ${PROG}
# This file is part of aboutjulietteattard
# Copyright (C) 2023 Juliette Attard
set -exvm
nvidia-settings --query CurrentMetaMode --display-device-string
if ( xrandr --listmonitors --verbose | grep "HDMI-0 connected 1x1"); then
nvidia-settings --assign CurrentMetaMode="HDMI-0: 4096x2160_60 +0+0 {viewportout=4016x2117+40+21, ForceCompositionPipeline=On}, DP-5: 1920x1080_60 +4016+0 {viewportin=1x1, viewportout=1x1+0+0}"
else
nvidia-settings --assign CurrentMetaMode="HDMI-0: 1920x1080 +1920+0 {viewportout=1x1+0+0}, DP-5: 1920x1080_60 +0+0 {ForceCompositionPipeline=On}"
fi
# service gdm3 restart
