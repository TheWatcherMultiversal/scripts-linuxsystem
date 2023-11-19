#!/bin/bash
#
# Installation and configuration script
# 
# Author: Angel Gabriel Mortera Gual
# License: GNU GENERAL PUBLIC LICENSE v3
#
# Project: https://github.com/TheWatcherMultiversal/scripts-linuxsystem/
#
# ----------------------------------------------------------------------------------------------------------------

PATH_LOCAL_BIN="$HOME/.local/bin"
ID_CURRENT_USER=`id -u`

if [ "$ID_CURRENT_USER" -eq "0" ]; then
	echo -e "\e[31mError:\e[0m Do not execute the script as root"
	exit 1
fi


case "$1" in
-u)
	# -> Uninstall scripts
	echo -e "\n\e[31mUninstall scripts...\e[0m\n"

	rm -vf "$PATH_LOCAL_BIN/audit-system"
	rm -vf "$PATH_LOCAL_BIN/scripts_systemTools.py"
	rm -vf "$PATH_LOCAL_BIN/scripts_systemUtils.py"
	rm -vf "$PATH_LOCAL_BIN/scripts-manage"
	rm -vf "$PATH_LOCAL_BIN/update-packages"

	echo -e "\n\e[32mEnd process...\e[0m\n"
	;;
--help)
	# -> Help message:
	echo """
usage: install.sh [-h] [-u]

options:
  -h, --help            show this help message and exit
  -u, --uninstall       uninstall scripts
	"""
	;;
*)
	# -> Installation of the scripts
	echo -e "\n\e[32mThe installation process has started, use this same executable with the \e[0m-u\e[32m option to reverse the process.\e[0m\n"

	echo -e "\e[33mCopying files to the local binary path...\e[0m\n"
	chmod 755 ./code/* && cp -vf ./code/* "$PATH_LOCAL_BIN/"

	echo -e "\n\e[33mRenaming files...\e[0m\n"
	mv -vf "$PATH_LOCAL_BIN/audit-system.py"    "$PATH_LOCAL_BIN/audit-system"
	mv -vf "$PATH_LOCAL_BIN/update-packages.py" "$PATH_LOCAL_BIN/update-packages"
	mv -vf "$PATH_LOCAL_BIN/scripts-manage.py"  "$PATH_LOCAL_BIN/scripts-manage"

	echo -e "\n\e[32mEnd process...\e[0m\n"
esac