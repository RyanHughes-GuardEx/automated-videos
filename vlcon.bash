#!/bin/bash

# without GUI
#/Applications/VLC.app/Contents/MacOS/VLC --intf telnet --telnet-password admin

# with GUI
/Applications/VLC.app/Contents/MacOS/VLC --extraintf telnet --telnet-password admin
python runvlc.py