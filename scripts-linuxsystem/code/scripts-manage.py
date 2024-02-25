#! /usr/bin/python3
#
# scripts_linuxsystem - scripts-manage
# 
# Command to manage all scripts in an intuitive way
#
# Author: Angel Gabriel Mortera Gual
# License: GNU GENERAL PUBLIC LICENSE v3
#
# Project: https://github.com/TheWatcherMultiversal/scripts-linuxsystem/
#
# ----------------------------------------------------------------------------------------------------------------

from scripts_systemTools import (auditSystem, updatePackages, videoDownload, subprocess, sys, os, sleep)
from scripts_systemUtils import (version, reset_color, print_list, print_info, print_error, green, cyan, red, yellow)

# ----------------------------------------------------------------------------------------------------------------
#   |
#   |
#   °-- Code:

# Path to script logs:
scripts_path = ("/.scripts-linuxsystem")


# Script main header:
def print_app():

    subprocess.run('clear', shell=True)
    title = r"""
                   _       _                              ___ _                  
     ___  ___ _ __(_)_ __ | |_ ___    __ _ _ __  _   _   / / (_)_ __  _   ___  __
    / __|/ __| '__| | '_ \| __/ __|  / _` | '_ \| | | | / /| | | '_ \| | | \ \/ /
    \__ \ (__| |  | | |_) | |_\__ \ | (_| | | | | |_| |/ / | | | | | | |_| |>  < 
    |___/\___|_|  |_| .__/ \__|___/  \__, |_| |_|\__,_/_/  |_|_|_| |_|\__,_/_/\_\
                    |_|              |___/     """
    
    inf = f"""
    {yellow + 'GitHub       :' + reset_color} {cyan + 'https://github.com/TheWatcherMultiversal/scripts-linuxsystem/' + reset_color}
    {yellow + 'License      :' + reset_color} {cyan + 'GNU General Public License v3.0' + reset_color}
    {yellow + 'Developed by :' + reset_color} {cyan + 'Angel Gabriel Mortera Gual' + reset_color}
"""
    print(green + title + reset_color); print(inf)
    

# --------------------------------------------------------------------------------------------------


# Prints the options and returns the chosen value:
def print_options(options:list, type='Options'):
    print('    > ' + cyan + f'{type}:\n' + reset_color)
    for i, item in enumerate(options): print('   ', end=''); print_list(i+1, item)
    return input('\nSelect an option: ')


# Prints the options of audit_option:
def audit_option():
    while True:
        print_app()
        opt = print_options(['audit system using available tools', 'view logs', 'return'])

        # --> audit system using available tools:
        if opt == '1': 
            try:
                subprocess.run('clear', shell=True)
                audit_system = auditSystem(HOME_CURRENT_USER, arg_y=False)
                if ID_CURRENT_USER != 0: audit_system.audit('sudo')
                else: audit_system.audit()
            except KeyboardInterrupt: pass

        # --> view logs:
        elif opt == '2' : 
            try: view_logs()
            except KeyboardInterrupt: pass

        # --> return:
        elif opt == '3' : break


# View logs:
def view_logs():
    logs_files = os.listdir(f'{HOME_CURRENT_USER}{scripts_path}/audits/')
    if not logs_files: print_info('No entries found'); sleep(3); return
    logs_files.append('return')

    while True:
        print_app()
        try:
            opt = int(print_options(logs_files, type='Files'))
            if logs_files[opt - 1] == 'return': break
            else: view_audit_log(logs_files[opt - 1])

        except: continue


# Opens the selected audit log:
def view_audit_log(file:str):
    if file[-3:] == 'txt':
        subprocess.run(f'gzip "{HOME_CURRENT_USER}{scripts_path}/audits/{file}"', shell=True); file += '.gz'

    subprocess.run('clear', shell=True)
    subprocess.run(f'gunzip "{HOME_CURRENT_USER}{scripts_path}/audits/{file}"',      shell=True)
    subprocess.run(f'more   "{HOME_CURRENT_USER}{scripts_path}/audits/{file[:-3]}"', shell=True)
    subprocess.run(f'gzip   "{HOME_CURRENT_USER}{scripts_path}/audits/{file[:-3]}"', shell=True)


# Runs system package updates:
def update_option():
    subprocess.run('clear', shell=True)
    update = updatePackages(arg_y=False)
    if ID_CURRENT_USER != 0: update.update_system('sudo')
    else: update.update_system()

# Download youtube video:
def down_video_option():
    while True:
        print_app()
        opt = print_options(['download video', 'download audio', 'return'])

        # --> download video:
        if opt == '1': 
            try:
                subprocess.run('clear', shell=True)
                source_video = input('\nLink video: ')
                videoDownload(source_video).down_video()
            except KeyboardInterrupt: pass

        # --> download audio:
        elif opt == '2' : 
            try:
                subprocess.run('clear', shell=True)
                source_video = input('\nLink video: ')
                videoDownload(source_video).down_audio()
            except KeyboardInterrupt: pass

        # --> return:
        elif opt == '3' : break
    
# ----------------------------------------------------------------------------------------------------------------
#   |
#   |
#   °-- Running the script:

if __name__ == "__main__":
    try:
        ID_CURRENT_USER   = int(str(subprocess.run('id -u',  shell=True, capture_output=True, text=True).stdout).replace("\n", ""))
        HOME_CURRENT_USER = str(subprocess.run('echo $HOME', shell=True, capture_output=True, text=True).stdout).replace("\n", "")
        while True:
            print_app()
            opt = print_options(['audit system', 'update system', 'download video/audio', 'exit'])

            if   opt == '1' : audit_option()
            elif opt == '2' : 
                try: update_option()
                except KeyboardInterrupt: pass
            elif opt == '3' : down_video_option()
            elif opt == '4' : sys.exit()
    except KeyboardInterrupt: os.system('clear'); sys.exit(1)
    except Exception as e: print_error(f'The code could not be executed, error found: {e}')