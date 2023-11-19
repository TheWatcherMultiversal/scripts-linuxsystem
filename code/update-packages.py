#! /usr/bin/python3
#
# scripts_linuxsystem - update-packages
# 
# Command to perform system package updates
#
# Author: Angel Gabriel Mortera Gual
# License: GNU GENERAL PUBLIC LICENSE v3
#
# Project: https://github.com/TheWatcherMultiversal/scripts-linuxsystem/
#
# ----------------------------------------------------------------------------------------------------------------

from scripts_systemTools import (updatePackages, subprocess, sys)
from scripts_systemUtils import (version)
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', metavar='[package-manager]',      help='select package manager')
parser.add_argument('-y', '--yes',     action='store_true', help='select yes by default')
parser.add_argument('-v', '--version', action='store_true', help='print version')
args = parser.parse_args()

if args.version : print(version); sys.exit(0)

if __name__ == "__main__":
    try:
        ID_CURRENT_USER   = int(str(subprocess.run('id -u',  shell=True, capture_output=True, text=True).stdout).replace("\n", ""))
        update = updatePackages(package_manager=args.p, arg_y=args.yes)
        if ID_CURRENT_USER != 0: update.update_system('sudo')
        else: update.update_system()
    except KeyboardInterrupt: sys.exit(1)