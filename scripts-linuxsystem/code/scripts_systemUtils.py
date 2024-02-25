#! /usr/bin/python3
#
# scripts_linuxsystem - scripts-manage
# 
# Module that adds available utilities and provides functions 
# for printing messages to the console or receiving user input
#
# Author: Angel Gabriel Mortera Gual
# License: GNU GENERAL PUBLIC LICENSE v3
#
# Project: https://github.com/TheWatcherMultiversal/scripts-linuxsystem/
#
# ----------------------------------------------------------------------------------------------------------------

from colorama import Fore
import sys

# ----------------------------------------------------------------------------------------------------------------
#   |
#   |
#   °-- Code:

version = 'v1.1.0'   # -> Version app
stderr  = sys.stderr # -> stderr
stdout  = sys.stdout # -> stdout

# Fore colors:
(red, green, blue, cyan, yellow) = (Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.YELLOW)
reset_color = Fore.RESET

# Packages Managers:
packages_managers = [
    'aptitude', 'apt', # -> DPKG
    'yum', 'dnf',      # -> RPM
    'pacman'           # -> ARCH
]

command_packagesManagers = {
    'aptitude' : ('aptitude update','aptitude safe-upgrade'),
    'apt'      : ('apt-get update','apt-get upgrade'),
    'yum'      : ('yum makecache','yum update'),
    'dnf'      : ('dnf makecache','yum update'),
    'pacman'   : ('pacman -Sy','pacman -Su'),
}

# Audit Tools:
audit_tools = [
    'lynis', 'rkhunter'
]

types_audits = {
    'lynis'    : ('lynis audit system'),
    'rkhunter' : ('rkhunter --check --sk'),
}

# Information messages
def print_notice(message, end=None)      : print(green + f'\n{message}\n' + reset_color,    file=stdout, end=end)
def print_info  (message, end=None, )    : print(yellow + 'Info: ' + reset_color + message, file=stdout, end=end) 
def print_error (message, end=None)      : print(red + 'ERROR: ' + reset_color + message,   file=stderr, end=end); sys.exit(1)
def print_list  (indice, item, end=None) : print(green + f'[{reset_color + str(indice) + green}] ' + reset_color + item, end=end)
def print_save  (file, end=None)         : print(green + '\nSave file: ' + cyan + file + '\n' + reset_color, file=stdout, end=end)

def input_confirm(message, confirm=False): 
    if confirm: return confirm
    else: print_info(message, end=' '); return input('[Y/n]: ').lower() == 'y'
