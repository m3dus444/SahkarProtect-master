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


class HandleSuspicious(FileSystemEventHandler):

    def on_modified(self, event):

        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'test':
                new_name = filename
                print("New suspect file is scuffed : " + filename)
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

                    #print("this is the new name with a number !  : " + new_name + '\n')
                    file_exists = os.path.isfile(folder_destination + "/" + new_name)
                    if i >= 20:
                        break

                src = folder_to_track + "/" + filename
                dst = folder_destination + "/" + new_name
                # print("this is the dst name : " + dst + '\n')
                # print("this is the src name : " + src + '\n')
                os.rename(src, dst)

    def on_deleted(self, event):

        """ If client delete download folder, it recreate itself automatically and restart the script"""

        try:
            time.sleep(0.1)
            old_name = folder_to_track
            os.mkdir(path=folder_to_track, mode=0o777)
            print("Don't try to delete that folder ! ")
            print(" Folder restaured, restarting process... ")
            exec(open("SuspiciousHandler.py").read())
        except:
            print("Your file has been sent for DMA ")

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
    key = key = wreg.OpenKey(wreg.HKEY_LOCAL_MACHINE, "Software\\Policies\\Google\\Chrome", 0, wreg.KEY_ALL_ACCESS)
    return wreg.QueryValueEx(key, 'DefaultDownloadDirectory')[0]





""" MAIN """

folder_to_track = getdownloadfolder()
folder_destination = "C:/users/" + getSessionUser.getuser(0) + "/Desktop/test"


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
