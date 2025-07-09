"""
plex_renamer.py
author/ Janus Wheatley
brief/ Bulk Rename Script for use in renaming TV Show season folders
about/ Plex requires the following naming for TV Shows
    [TV SHOW NAME]
        [SEASON X]
            [TV SHOW NAME + SEASON X + EPX]
            ...
how to/
    ARGS -> python plex_renamer.py "[FOLDER DIRECTORY]" "[TV SHOW NAME] [SEASON]"
    All files in the Folder Directory will be renamed to ARG 2 + their episode # which is counted
    The files MUST be in order naturally or they will be renamed w/ the wrong #
ex/
    python plex_renamer.py "E:\TV Shows\Clone Wars\Clone Wars S01" "Clone Wars S01"

This program is open source, feel free to edit/modify
"""
import sys
import os

if (len(sys.argv) == 3):
    directory = sys.argv[1]
    name = sys.argv[2]
    try:
        folder = os.listdir(path=directory)
        print("### OLD DIRECTORY ##")
        print(folder)
        for ep,old in enumerate(folder,1):
            ext = os.path.splitext(old)[1]
            new = name + " EP" + str(ep) + ext
            old_path = os.path.join(directory,old)
            new_path = os.path.join(directory,new)
            os.rename(old_path,new_path)
            print(old, " -> ", new)
        print("### NEW DIRECTORY ##")
        print(os.listdir(path=directory))
    except:
        print("ERROR: something went wrong")
else:
    print("ERROR: Requires", len(sys.argv), "arguments!")


