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
import server

class HandleSuspicious(FileSystemEventHandler):
    def __init__(self, folder_to_track, folder_destination):
        self.folder_to_track = folder_to_track
        self.folder_destination = folder_destination
        print("A new watchdog is awake !\r")

    def on_modified(self, event):
        """ This function run itself when the folder/subfolder/file in folder is moved in/ modified"""
        if os.path.isdir(self.folder_to_track):
            for filename in os.listdir(self.folder_to_track):
                i = 1
                if filename != self.folder_to_track and '.skp' not in filename:
                    new_name = filename

                    """ encryption before moving to server folder"""
                    print("New suspect file is scuffed : " + filename)
                    quanrtineHandler.encrypt(self.folder_to_track, filename)

                    file_exists = os.path.isfile(self.folder_destination + '/' + new_name)
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

                        file_exists = os.path.isfile(self.folder_destination + "/" + new_name)
                        if i >= 20:
                            break

                    src = self.folder_to_track + "/" + filename
                    dst = self.folder_destination + "/" + new_name
                    # print("this is the dst name : " + dst + '\n')
                    # print("this is the src name : " + src + '\n')

                    os.rename(src, dst)
                    time.sleep(0.2)
                    """ SENDING FOR DMA"""
                    server.execute_analysis("quick_scan_file", filename=new_name)
                    server.execute_analysis("sandbox_file", filename=new_name)
                    print("not blocked")
        else:
            print("Scrript noticed path dir is unreachable ! \r")
            self.on_deleted(self)

    def on_deleted(self, event):

        """ If client delete download folder, it recreate itself automatically and restart the script
            Plus, it also run itself once a file is sent for DMA in on_modified function because
            it deletes the file while moving it to server folder"""
        print("we get throught this instant after normally")
        try:
            time.sleep(0.1)
            if getSessionUser.getuser(0) in self.folder_to_track:
                os.mkdir(path=self.folder_to_track, mode=0o777)
                print("Don't try to delete that folder ! ")
                print(" Folder restaured, restarting process... ")
                start_observer(self.folder_to_track, self.folder_destination)
            else:
                print("Killing watchdog over flashdrive...")
                #close_observer() WIP as we dont have observer to pass in args
                sys.exit(__status="USB Key removed, killing process")
        except:
            print("Your file has been sent for DMA. You'll get it back in /Documents/ once checked.\r")

    def on_moved(self, event):
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
    key = wreg.OpenKey(wreg.HKEY_LOCAL_MACHINE, "Software\\Policies\\Google\\Chrome", 0, wreg.KEY_READ)
    return wreg.QueryValueEx(key, 'DefaultDownloadDirectory')[0]




def start_observer(folder_to_track, folder_destination):

    """ MAIN """

    event_handler = HandleSuspicious(folder_to_track, folder_destination)
    #print("Looking for suspicious files on : %s...\r" % folder_to_track)
    observer = Observer()
    #print("we get trought oberserver")
    observer.schedule(event_handler, path=folder_to_track, recursive=True)
    #print("we get trought schedule")
    try:
        observer.start()
        print("we get trought start")
    except:
        observer.stop()
        print(observer.join())

    try:
        while True:
            time.sleep(10)
            print("Looking for suspicious files on : %s...\r" % folder_to_track)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    return 0


def close_observer(observer):
    observer.stop()
    observer.join()


""" GENERAL CODE """
if len(sys.argv) > 2:
    start_observer(sys.argv[1], sys.argv[2])
else:
    print("we good to go without args")