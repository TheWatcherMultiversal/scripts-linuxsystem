#! /usr/bin/python3
#
# scripts_linuxsystem - scripts_systemTools
# 
# Module that includes scripts to manage a Linux system
#
# Author: Angel Gabriel Mortera Gual
# License: GNU GENERAL PUBLIC LICENSE v3
#
# Project: https://github.com/TheWatcherMultiversal/scripts-linuxsystem/
#
# ----------------------------------------------------------------------------------------------------------------

import sys, argparse, subprocess, os
from scripts_systemUtils import (print_error, print_notice, print_info, print_list, print_save,
    packages_managers, command_packagesManagers, input_confirm, audit_tools, types_audits)
from datetime import datetime
from time import sleep


# ----------------------------------------------------------------------------------------------------------------
#   |
#   |
#   °-- Code:

class updatePackages(object):

    # Define the command to run updates:
    def __init__(self, arg_y:bool, package_manager=None):

        # -> Checking for the existence of flatpak, snap or yay commands:
        self.flatpakExist = os.system('type flatpak > /dev/null') == 0
        self.snapExist    = os.system('type snap > /dev/null')    == 0
        self.yayExist     = os.system('type yay > /dev/null')     == 0
        self.confirm_yes  = arg_y

        try: 
            # --> Choose a package manager in case you choose one:
            if package_manager: self.command = command_packagesManagers[package_manager]; return

            # --> Store the package managers in case there are more than one:
            self.commands = [i for i in packages_managers if os.system(f'type {i} > /dev/null') == 0]
            if len(self.commands) > 1: self.choice_packageManager()
            else: self.command = command_packagesManagers[self.commands[0]]
        except KeyError: print_error('Package manager not found')
    

    # Method to choose a single package manager:
    def choice_packageManager(self):
        print_info('You should select only one package manager to proceed')
        for i, command in enumerate(self.commands):
            print_list(i + 1, command)
            
        try: 
            opt          = int(input('select an option: '))
            command      = self.commands[opt - 1]
            self.command = command_packagesManagers[command]
            return

        except ValueError: print_error(f'Enter a numerical value')
        except IndexError: print_error(f'This value is not in the list')


    # Update the system packages:
    def update_system(self, sudo=''):
        try:
            # --> Resynchronize the package index files from their sources:
            print_notice('Resynchronize the package index files from their sources...')
            subprocess.run(f'{sudo} {self.command[0]}', shell=True, check=True)

            # --> Install the newest versions of all packages:
            print_notice('Install the newest versions of all packages...')
            subprocess.run(f'{sudo} {self.command[1]}', shell=True, check=True)

            # --> In case they exist, update as well:
            if self.flatpakExist : self.update_flatpak()
            if self.snapExist    : self.update_snap(sudo)
            if self.yayExist     : self.update_aur()
    
            print_notice('End process...'); sleep(2)

        except subprocess.CalledProcessError: print_error('An error occurred during the package update, please try again')
        except Exception as e: print_error(f'The code could not be executed, error found: {e}')


    # Update flatpak packages:
    def update_flatpak(self):
        opt = input_confirm('Do you want to update the flatpak packages?', self.confirm_yes)
        if opt: print_notice('Updating flatpak packages...'); subprocess.run('flatpak update', shell=True, check=True)


    # Update snap packages:
    def update_snap(self, sudo):
        opt = input_confirm('Do you want to update the snap packages?', self.confirm_yes)
        if opt: print_notice('Updating snap packages...'); subprocess.run(f'{sudo} snap refresh', shell=True, check=True)


    # Update AUR packages
    def update_aur(self): #-> Using yay
        opt = input_confirm('Do you want to update the snap packages?', self.confirm_yes)
        if opt: print_notice('Updating flatpak packages...'); subprocess.run('yay -Syu', shell=True, check=True)


class auditSystem(object):


    # Class initial configuration:
    def __init__(self, home_directory, arg_y:bool):
        self.audit_tools = [i for i in audit_tools if os.system(f'type {i} > /dev/null') == 0]
        self.home_directory = home_directory
        self.confirm_yes = arg_y


    # Detects the existing utilities in the system:
    def audit(self, sudo=''):
        print_info('Audit tools detected:')
        for i, item in enumerate(self.audit_tools): print_list(i + 1, item)

        # -> If available, execute the utility:
        print_notice('Audit system...')
        if audit_tools: 
            for audit_tool in audit_tools: self.audit_withTool(audit_tool, sudo)

        print_notice('End process...'); sleep(2)



    # Perform the audit using the utility:
    def audit_withTool(self, type_audit, sudo=''):
        opt = input_confirm(f'Do you want to perform a system audit with {type_audit}?', self.confirm_yes)
        if opt: 
            print_notice(f'Auditing the system with {type_audit}...')
            process = subprocess.Popen(f'{sudo} {types_audits[type_audit]}', shell=True, stdout=subprocess.PIPE, text=True)
            stdout = ''

            for line in process.stdout: stdout += line; print(line, end='')
            process.wait()

            # --> Save audit output to a file" o "Store the audit results in a file:
            opt = input_confirm('Do you want to store the information in a file?', self.confirm_yes)
            if opt:
                date = datetime.now()
                save_audit = f'{self.home_directory}/.scripts-linuxsystem/audits/audit_{type_audit}_{date.date()}_{date.hour}-{date.minute}-{date.second}.txt'
                with open(save_audit, 'w') as file: file.write(stdout)
                subprocess.run(f'gzip {save_audit}', shell=True, check=True); print_save(save_audit)
