#! /usr/bin/env python3
#! /usr/bin/env python3
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import os
import time
import sys
import getSessionUser
import quanrtineHandler
from multiprocessing.pool import ThreadPool
import server
import canvas
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
                    # print("this is the dst name : " + dst + '\n')
                    # print("this is the src name : " + src + '\n')

                    shutil.move(src, dst)
                    #os.rename(src, dst)
                    #shutil.move(r"E:\\fgdg.txt", r"C:\users\julie\Desktop\fgdg2.txt") -> yes
                    time.sleep(0.2)
                    """ SENDING FOR DMA AND SET DMA VAR"""
                    self.async_returns_hybrid.append(self.pool_hybrid_analysis.apply_async(server.execute_analysis, (
                                "quick_scan_file", None, new_name)))
                    HandleSuspicious.SMA_started.append(1)
                    #self.async_returns_hybrid.append(self.pool_hybrid_analysis.apply_async(server.execute_analysis, (
                    #            "sandbox_file", None, new_name)))
                    #HandleSuspicious.DMA_started.append(1)

                    HandleSuspicious.deleted_or_sent = 1
                    #print("NOT BLOCKED")
        else:
            xprint()
            print("Watchdog CAN'T see the folder to track anymore! \r")
            self.on_deleted(self)

    def on_deleted(self, event):

        """ If client delete download folder, it recreate itself automatically and restart the script
            Plus, it also run itself every time a file is sent for DMA in on_modified function because
            it deletes the file while moving it to server folder. We have to draw a between sending DMA
            cases, USB Removing cases and RM Download folder cases. That's the reason of all the conditions """

        try:
            time.sleep(0.1) #we wait because
            print("len dir USB: ", len(self.folder_to_track))
            print("dir can be reach: ", os.path.isdir(self.folder_to_track))
            if getSessionUser.getuser(0) in self.folder_to_track and not os.path.isdir(self.folder_to_track):
                os.mkdir(path=self.folder_to_track, mode=0o777)
                print("Don't try to delete that folder ! ")
                print(" Folder restored, restarting process... ")
                start_observer(self.folder_to_track, self.folder_destination, self.folder_documents)

            elif len(self.folder_to_track) < 5 and not os.path.isdir(self.folder_to_track):
                xprint()
                print("A flashdrive device was REMOVED !")
                print("Killing watchdog over flashdrive...")
                #close_observer() WIP as we dont have observer to pass in args
                return 1
                #sys.exit(__status="USB Key removed, killing process")

        except:
            print("Couldn't restore download folder or kill process !\r")

        if HandleSuspicious.deleted_or_sent == 1:
            print("Your file has been sent for SMA and DMA. You'll get it back in /Documents/ once checked.\r")
        else:
            xprint()
            print("One of your file just came back from SMA !\r")

    def on_moved(self, event):
        """ if the folder is moved, we try to get its new path !!!WIP!!!

        evasion_path =
        print(evasion_path)
        os.rename(evasion_path, folder_to_track)

        """

    def on_created(self, event):
        """ WTD ? """
        print("ON CREATED JUST GET ACTIVATED")

    def SMA(self):
        try:
            print("len des reponses: ", len(self.async_returns_hybrid))
            print("status du premier elem: ", self.async_returns_hybrid[0])
            print("HandleSuspicious.SMA_started[0]: ", HandleSuspicious.SMA_started[0].ready())
            print("deleted or sent: ", HandleSuspicious.deleted_or_sent)
        except:
            print("toutes les conditions ne sont pas réunies")

        if len(self.async_returns_hybrid) > 0 and self.async_returns_hybrid[0].ready() and HandleSuspicious.SMA_started[0]:
            print("1")
            HandleSuspicious.deleted_or_sent = 0  # allow to know when a file is sent for DMA from DL folder and when it is decrypted. We dont print the same thing
            print("2")
            keepquarantine = self.async_returns_hybrid[0].get()
            print("3")
            print("One of your file has been analysed\r")
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
                print("SMA status can't be established")

            self.scuffed_files.remove(self.scuffed_files[0])
            self.async_returns_hybrid.remove(self.async_returns_hybrid[0])
            HandleSuspicious.SMA_started.remove(HandleSuspicious.SMA_started[0])

    def DMA(self):
        if len(self.async_returns_hybrid) > 0 and self.async_returns_hybrid[1].ready() and HandleSuspicious.DMA_started[0]:

            HandleSuspicious.deleted_or_sent = 0  # allow to know when a file is sent for DMA from DL folder and when it is decrypted. We dont print the same thing
            keepquarantine = self.async_returns_hybrid[1].get()

            print("One of your file has been analysed\r")
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
    status = 0
    try:
        #shutil.chown(folder_to_track, 'julie')
        status = observer.start()
    except:
        observer.stop()
        print(observer.join())

    try:
        time.sleep(3)
        print_count = 0
        while status != 1:
            if len(event_handler.async_returns_hybrid) > 0 and event_handler.async_returns_hybrid[0].ready() and HandleSuspicious.SMA_started[0]:
                print("1")
                print("status ready :", event_handler.async_returns_hybrid[0].ready())
                print("2")
                proc = event_handler.async_returns_hybrid[0]
                print("proc : ", proc)
                keepquarantine = proc.get()
                print("3")
                print("keep quarantine : ", keepquarantine)
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
                event_handler.deleted_or_sent = 0  # allow to know when a file is sent for DMA from DL folder and when it is decrypted. We dont print the same thing
            #event_handler.SMA()
            #event_handler.DMA()
            time.sleep(2)
            print_count += 1
            if print_count % 5 == 0:
                print("Looking for suspicious files on : %s...\r" % folder_to_track)
    except KeyboardInterrupt:
        print("KBM Interruption worked on watchdog process !")
    observer.stop()
    observer.join()
    xprint()
    print("Returning status due to flashdrive remove")
    return status


def close_observer(observer):
    observer.stop()
    observer.join()


""" GENERAL CODE """
if len(sys.argv) > 2:
    start_observer(sys.argv[1], sys.argv[2], sys.argv[3])



