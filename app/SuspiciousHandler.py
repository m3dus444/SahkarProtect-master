#! /usr/bin/env python3

from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import sys
import ctypes
import json
import shutil
import getSessionUser
import quanrtineHandler


class HandleSuspicious(FileSystemEventHandler):

    def on_modified(self, event):
        """ This function run itself when the folder/subfolder/file in folder is moved in/ modified"""

        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'test' and '.skp' not in filename:
                new_name = filename

                """ encryption before moving to server folder"""
                print("New suspect file is scuffed : " + filename)
                quanrtineHandler.encrypt(folder_to_track, filename)

                file_exists = os.path.isfile(folder_destination + '/' + new_name)
                while file_exists:
                    i += 1

                    if i > 2:
                        """ We replace then  number indicator of the copy by i+1"""

                        k = new_name.rfind("_")
                        new_name = new_name[:k] + "_" + new_name[k + 1:].replace(str(i - 1), str(i))

                    else:
                        """ If it's the first copy we do this nomenclature : file_2"""

                        new_name = os.path.splitext(new_name)[0] + "_" + str(i) + \
                                   os.path.splitext(new_name)[1]

                    file_exists = os.path.isfile(folder_destination + "/" + new_name)
                    if i >= 20:
                        break

                src = folder_to_track + "/" + filename
                dst = folder_destination + "/" + new_name
                # print("this is the dst name : " + dst + '\n')
                # print("this is the src name : " + src + '\n')
                os.rename(src, dst)

    def on_deleted(self, event):

        """ If client delete download folder, it recreate itself automatically and restart the script
            Plus, it also run itself once a file is sent for DMA in on_modified function because
            it deletes the file while moving it to server folder"""

        try:
            time.sleep(0.1)
            old_name = folder_to_track
            os.mkdir(path=folder_to_track, mode=0o777)
            print("Don't try to delete that folder ! ")
            print(" Folder restaured, restarting process... ")
            exec(open("SuspiciousHandler.py").read())
        except:
            print("Your file has been sent for DMA. You'll get it back in /Documents/ once checked.")

    def on_moved(self, event):
        print("moved")

        """ if the folder is moved, we try to get its new path !!!WIP!!!

        evasion_path = os.getcwd()
        print(evasion_path)
        os.rename(evasion_path, folder_to_track)

        """

    def on_created(self, event):
        """ WTD ? """


def getdownloadfolder():
    if sys.version[0] == '2':
        input = raw_input
        import _winreg as wreg
    else:
        import winreg as wreg
    key = key = wreg.OpenKey(wreg.HKEY_LOCAL_MACHINE, "Software\\Policies\\Google\\Chrome", 0, wreg.KEY_READ)
    return wreg.QueryValueEx(key, 'DefaultDownloadDirectory')[0]





""" MAIN """

folder_to_track = getdownloadfolder()
folder_destination = r"C:\users\\" + getSessionUser.getuser(0) + r"\Desktop\test"
folder_device = 'device'

event_handler = HandleSuspicious()
observer = Observer()
observer.schedule(event_handler, path=folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
