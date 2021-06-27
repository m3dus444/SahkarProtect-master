
#! /usr/bin/env python3
#! /usr/bin/env python3
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import os
import time
import sys
#sys.path.insert(0,'C:/Users/julie/PycharmProjects/SahkarProtect-master/app')
import getSessionUser
import quanrtineHandler
from multiprocessing.pool import ThreadPool
import server
from canvas import xprint as xprint


class HandleSuspicious(FileSystemEventHandler):
    """ This is the watchdog class. We're not saving logs here, so in order to remembers which file we sent
    to DMA and SMA we store them in a list just bellow. As far as we know, our results from MA are FIFO based.
    In other words, the first file we'll send will be the first one to have its get.ready() TRUE.
    That's why we only check index 0 of SMA/DMA/scuffed lists. Once we handle the status and so the file, we just
    remove work assignment at index 0 of all lists. """

    deleted_or_sent = 0
    scuffed_files = []
    SMA_started = []
    DMA_started = []

    def __init__(self, folder_to_track, folder_destination, folder_documents, pool_hybrid_analysis, async_returns_hybrid):
        self.folder_to_track = folder_to_track
        self.folder_destination = folder_destination
        self.folder_documents = folder_documents
        self.pool_hybrid_analysis = pool_hybrid_analysis
        self.async_returns_hybrid = async_returns_hybrid
        xprint()
        print("A new watchdog is awake !\r")
        print("Looking for suspicious files on : %s...\r" % folder_to_track)

    def on_modified(self, event):
        """ This function run itself when the folder/subfolder/file in folder is moved in/ modified"""
        if os.path.isdir(self.folder_to_track):
            for filename in os.listdir(self.folder_to_track):
                i = 1
                if filename != self.folder_to_track and filename != 'System Volume Information' and '.skp' not in filename:

                    new_name = filename
                    xprint()
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
                    HandleSuspicious.scuffed_files.append(new_name)
                    print(" list of current scuffed files : ", self.scuffed_files)
                    quanrtineHandler.encrypt(self.folder_to_track, filename, new_name)
                    src = self.folder_to_track + "/" + filename
                    dst = self.folder_destination + "/" + new_name

                    shutil.move(src, dst)
                    #os.rename(src, dst)
                    #shutil.move(r"E:\\fgdg.txt", r"C:\users\julie\Desktop\fgdg2.txt") -> yes
                    time.sleep(0.25)

                    """ SENDING FOR DMA AND SET DMA VAR"""
                    self.async_returns_hybrid.append(self.pool_hybrid_analysis.apply_async(server.execute_analysis, (
                                "quick_scan_file", None, new_name)))
                    HandleSuspicious.SMA_started.append(1)
                    time.sleep(1)
                    #self.async_returns_hybrid.append(self.pool_hybrid_analysis.apply_async(server.execute_analysis, (
                    #            "sandbox_file", None, new_name)))
                    #HandleSuspicious.DMA_started.append(1)

                    print("Your file has been sent for SMA and DMA. You'll get it back in /Documents/ once checked.\r")


        else:
            print("Watchdog CAN'T see the folder to track anymore! \r")
            self.on_deleted(event)

    def on_deleted(self, event):
        print("ON DELETED")

        """ If client delete download folder, it recreate itself automatically and restart the script
            Plus, it also run itself every time a file is sent for DMA in on_modified function because
            it deletes the file while moving it to server folder. We have to draw a between sending DMA
            cases, USB Removing cases and RM Download folder cases. That's the reason of all the conditions """

        try:
            time.sleep(0.1) #we wait because
            if getSessionUser.getuser(0) in self.folder_to_track and not os.path.isdir(self.folder_to_track):
                os.mkdir(path=self.folder_to_track, mode=0o777)
                print("Don't try to delete that folder ! ")
                print(" Folder restored, restarting process... ")
                #start_observer(self.folder_to_track, self.folder_destination, self.folder_documents)

        except:
            print("Couldn't restore download folder, killing process !\r")
            sys.exit()


    def on_moved(self, event):
        """ if the folder is moved, we try to get its new path

        """

    def on_created(self, event):
        """ WTD ? """
        """for download in os.listdir(self.folder_to_track):
            if '.skp' not in download:
                print("Your download has been sent for SMA and DMA")"""

    def on_removed(self):
        if len(self.folder_to_track) < 5 and not os.path.isdir(self.folder_to_track):
            xprint()
            print("A flashdrive device was REMOVED !")
            print("Killing watchdog over flashdrive...")
            sys.exit()

    def SMA(self):
        if len(self.async_returns_hybrid) > 0 and self.async_returns_hybrid[0].ready() and HandleSuspicious.SMA_started[0]:
            keepquarantine = self.async_returns_hybrid[0].get()
            print("Your file %s is a clear file !\r" % self.scuffed_files[0])
            if keepquarantine == 0:
                os.remove(os.getcwd() + r"\\uploadServer\\" + self.scuffed_files[0])
                quanrtineHandler.decrypt(self.folder_to_track, self.scuffed_files[0],
                                         self.folder_documents)
                """ if .exe call DMA"""

            elif keepquarantine == 1:
                print("Your file %s has been revealed to be a Ransomware/Malware !\r" % self.scuffed_files[0])
                os.remove(getdownloadfolder() + r"\\" + self.scuffed_files[0])
                os.remove(os.getcwd() + r"\\encryption\quarantineKey_" + self.scuffed_files[0] + '.skk')
                quanrtineHandler.encrypt(os.getcwd() + r"\\uploadServer\\", self.scuffed_files[0],
                                         self.scuffed_files[0])

            else:
                print("SMA status of your file %s can't be established" % self.scuffed_files[0])
                """ if .exe call DMA"""

            self.scuffed_files.remove(self.scuffed_files[0])
            self.async_returns_hybrid.remove(self.async_returns_hybrid[0])
            HandleSuspicious.SMA_started.remove(HandleSuspicious.SMA_started[0])

    def DMA(self):
        if len(self.async_returns_hybrid) > 0 and self.async_returns_hybrid[1].ready() and HandleSuspicious.DMA_started[0]:
            keepquarantine = self.async_returns_hybrid[1].get()

            print("Your file %s is a clear file !\r" % self.scuffed_files[0])
            print(" keep quarantine : %s \r" % str(keepquarantine))

            if keepquarantine == 0:
                os.remove(os.getcwd() + r"\\uploadServer\\" + self.scuffed_files[0])
                quanrtineHandler.decrypt(self.folder_to_track, self.scuffed_files[0],
                                         self.folder_documents)

            elif keepquarantine == 1:
                print("Your file %s has been revealed to be a Ransomware/Malware !\r" % self.scuffed_files[0])
                os.remove(getdownloadfolder() + r"\\" + self.scuffed_files[0])
                os.remove(os.getcwd() + r"\\encryption\quarantineKey_" + self.scuffed_files[0] + '.skk')
                quanrtineHandler.encrypt(os.getcwd() + r"\\uploadServer\\", self.scuffed_files[0],
                                         self.scuffed_files[0])

            else:
                print("DMA status can't be established")
            self.scuffed_files.remove(self.scuffed_files[0])
            self.async_returns_hybrid.remove(self.async_returns_hybrid[0])
            HandleSuspicious.DMA_started.remove(HandleSuspicious.DMA_started[0])



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

    pool_hybrid_analysis = ThreadPool(processes=5)
    async_returns_hybrid = []
    event_handler = HandleSuspicious(folder_to_track, folder_destination, folder_documents, pool_hybrid_analysis, async_returns_hybrid)
    observer = Observer()
    observer.schedule(event_handler, path=folder_to_track, recursive=True)
    try:
        observer.start()
        time.sleep(2)
    except:
        observer.stop()
        print(observer.join())

    try:
        print_count = 0
        while True:
            event_handler.on_removed()
            time.sleep(5)
            event_handler.SMA()
            #event_handler.DMA()
            print_count += 1
            if print_count % 5 == 0:
                print("Looking for suspicious files on : %s...\r" % folder_to_track)
    except KeyboardInterrupt:
        print("KBM Interruption from watchdog process.")
    observer.stop()
    observer.join()
    xprint()


""" GENERAL CODE """
if __name__ == '__main__':
    if len(sys.argv) > 2:
        start_observer(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Arguments missing ! \n")