#!/bin/bash

# without GUI
#/Applications/VLC.app/Contents/MacOS/VLC --intf telnet --telnet-password admin

# with GUI
/Applications/VLC.app/Contents/MacOS/VLC --extraintf telnet --telnet-password admin &
sleep 1     # need to wait for telnet to turn on
python runvlc.py
osascript -e 'quit app "VLC"'