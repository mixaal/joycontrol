#!/bin/bash -x

sudo nohup python3 run_emu.py PRO_CONTROLLER &
nohup python3 gamepad.py &

xset r off
python3 kbd_hold_release.py
xset r on

