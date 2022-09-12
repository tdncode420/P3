'''Upgrade pip to latest version

    A simple script to upgrade python's pip (per OS) to it's latest version

'''

import os, sys

def Run():
    platform = sys.platform
    if platform == 'win32':
        cmd = 'py -m pip install --upgrade pip'
    else:
        cmd = 'python3 -m pip install --upgrade pip'
    cmdrun = os.popen(cmd)
    output = cmdrun.read()
    return output