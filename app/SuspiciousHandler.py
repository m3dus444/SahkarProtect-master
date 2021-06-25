#! /usr/bin/env python3
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
from multiprocessing.pool import ThreadPool
import server
import asyncio
import subprocess

class HandleSuspicious(FileSystemEventHandler):
    deleted_or_sent = 0
    def __init__(self, folder_to_track, folder_destination, folder_documents, scuffed_files, pool_hybrid_analysis, async_returns_hybrid):
        self.folder_to_track = folder_to_track
        self.folder_destination = folder_destination
        self.folder_documents = folder_documents
        self.scuffed_files = scuffed_files
        self.pool_hybrid_analysis = pool_hybrid_analysis
        self.async_returns_hybrid = async_returns_hybrid
        print("A new watchdog is awake !\r")

    def on_modified(self, event):
        """ This function run itself when the folder/subfolder/file in folder is moved in/ modified"""
        if os.path.isdir(self.folder_to_track):
            for filename in os.listdir(self.folder_to_track):
                i = 1
                if filename != self.folder_to_track and '.skp' not in filename:

                    new_name = filename
                    print("New suspect file is scuffed : " + filename)

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
                    self.scuffed_files.append(new_name)
                    print(" list of scuffed files : ", self.scuffed_files)
                    quanrtineHandler.encrypt(self.folder_to_track, filename, new_name)
                    src = self.folder_to_track + "/" + filename
                    dst = self.folder_destination + "/" + new_name
                    # print("this is the dst name : " + dst + '\n')
                    # print("this is the src name : " + src + '\n')

                    os.rename(src, dst)
                    time.sleep(0.2)
                    """ SENDING FOR DMA AND SET DMA VAR"""
                    self.async_returns_hybrid.append(self.pool_hybrid_analysis.apply_async(server.execute_analysis, ("quick_scan_file", None, new_name)))
                    HandleSuspicious.deleted_or_sent = 1
                    print("NOT BLOCKED")
        else:
            print("Given script dir is unreachable for watchdog ! \r")
            self.on_deleted(self)

    def on_deleted(self, event):

        """ If client delete download folder, it recreate itself automatically and restart the script
            Plus, it also run itself once a file is sent for DMA in on_modified function because
            it deletes the file while moving it to server folder"""

        try:
            time.sleep(0.1)
            if getSessionUser.getuser(0) in self.folder_to_track and not os.path.isdir(self.folder_to_track):
                os.mkdir(path=self.folder_to_track, mode=0o777)
                print("Don't try to delete that folder ! ")
                print(" Folder restored, restarting process... ")
                start_observer(self.folder_to_track, self.folder_destination, self.folder_documents)
            elif len(self.folder_to_track) < 5 and not os.path.isdir(self.folder_to_track):
                print("Killing watchdog over flashdrive...")
                #close_observer() WIP as we dont have observer to pass in args
                sys.exit(__status="USB Key removed, killing process")

        except:
            print("Couldn't restore download folder or kill process.\r")

        if HandleSuspicious.deleted_or_sent == 1:
            print("Your file has been sent for DMA. You'll get it back in /Documents/ once checked.\r")
        else:
            print("One of your file just came back from DMA !\r")

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




def start_observer(folder_to_track, folder_destination, folder_documents):

    """ MAIN """
    #n = 5
    scuffed_files = []
    pool_hybrid_analysis = ThreadPool(processes=5)
    async_returns_hybrid = []
    event_handler = HandleSuspicious(folder_to_track, folder_destination, folder_documents, scuffed_files, pool_hybrid_analysis, async_returns_hybrid)
    observer = Observer()
    observer.schedule(event_handler, path=folder_to_track, recursive=True)
    try:
        observer.start()
        print("we get trought start")
    except:
        observer.stop()
        print(observer.join())

    try:
        while True:
            #print(" ready status : ", event_handler.async_returns_hybrid[0].ready())
            if len(event_handler.async_returns_hybrid) > 0 and event_handler.async_returns_hybrid[0].ready():
                event_handler.deleted_or_sent = 0  # allow to know when a file is sent for DMA from DL folder and when it is decrypted. We dont print the same thing
                keepquarantine = event_handler.async_returns_hybrid[0].get()
                print("One of your file has been analysed\r")
                print(" keep quarantine : %s \r" % str(keepquarantine))
                if keepquarantine == 0:
                    os.remove(os.getcwd() + r"\\uploadServer\\" + event_handler.scuffed_files[0])
                    quanrtineHandler.decrypt(event_handler.folder_to_track, event_handler.scuffed_files[0], event_handler.folder_documents)

                elif keepquarantine == 1:
                    print("Your file %s has been revealed to be a Ransomware/Malware !\r" % event_handler.scuffed_files[0])
                    os.remove(getdownloadfolder() + r"\\" + event_handler.scuffed_files[0])
                    os.remove(os.getcwd() + r"\\encryption\quarantineKey_" + event_handler.scuffed_files[0] + '.skk')
                    quanrtineHandler.encrypt(os.getcwd() + r"\\uploadServer\\", event_handler.scuffed_files[0],
                                             event_handler.scuffed_files[0])
                event_handler.scuffed_files.remove(event_handler.scuffed_files[0])
                event_handler.async_returns_hybrid.remove(event_handler.async_returns_hybrid[0])

            time.sleep(3)
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
    start_observer(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    print("we good to go without args")