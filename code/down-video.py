#! /usr/bin/python3
#
# scripts_linuxsystem - down-audio
# 
# Command to download a video or audio from YouTube
# using youtube-dl and ffmpeg
#
# Author: Angel Gabriel Mortera Gual
# License: GNU GENERAL PUBLIC LICENSE v3
#
# Project: https://github.com/TheWatcherMultiversal/scripts-linuxsystem/
#
# ----------------------------------------------------------------------------------------------------------------

from scripts_systemTools import (videoDownload, subprocess, sys)
from scripts_systemUtils import (version)
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('link',            nargs='*',              help='link to the YouTube video')
parser.add_argument('-a',              metavar='[link]',       help='download the audio from the link')
parser.add_argument('-v', '--version', action='store_true',    help='print version')
args = parser.parse_args()

if args.version : print(version); sys.exit(0)

if __name__ == "__main__":
    try:
        if   args.link : source_video = args.link[0] ; videoDownload(source_video).down_video()
        elif args.a    : source_video = args.a       ; videoDownload(source_video).down_audio()
    except KeyboardInterrupt: sys.exit(1)