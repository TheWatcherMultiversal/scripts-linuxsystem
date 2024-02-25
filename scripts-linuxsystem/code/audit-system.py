#! /usr/bin/python3
#
# scripts_linuxsystem - audit-system
# 
# Command to initialize an audit with the existing 
# tools in the system
#
# Author: Angel Gabriel Mortera Gual
# License: GNU GENERAL PUBLIC LICENSE v3
#
# Project: https://github.com/TheWatcherMultiversal/scripts-linuxsystem/
#
# ----------------------------------------------------------------------------------------------------------------

from scripts_systemTools import (auditSystem, subprocess, sys)
from scripts_systemUtils import (version)
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-y', '--yes',     action='store_true', help='select yes by default')
parser.add_argument('-v', '--version', action='store_true', help='print version')
args = parser.parse_args()

if args.version : print(version); sys.exit(0)

if __name__ == "__main__":
    try:
        ID_CURRENT_USER   = int(str(subprocess.run('id -u',  shell=True, capture_output=True, text=True).stdout).replace("\n", ""))
        HOME_CURRENT_USER = str(subprocess.run('echo $HOME', shell=True, capture_output=True, text=True).stdout).replace("\n", "")
        audit = auditSystem(HOME_CURRENT_USER, args.yes)
        if ID_CURRENT_USER != 0: audit.audit('sudo')
        else: audit.audit()
    except KeyboardInterrupt: sys.exit(1)