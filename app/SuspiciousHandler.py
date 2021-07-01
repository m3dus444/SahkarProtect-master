
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
import extensions


class HandleSuspicious(FileSystemEventHandler):
    """ This is the watchdog class. We're not saving logs here, so in order to remembers which file we sent
    to DMA and SMA we store them in a list just bellow. As far as we know, our results from MA are FIFO based.
    In other words, the first file we'll send will be the first one to have its get.ready() TRUE.
    That's why we only check index 0 of SMA/DMA/scuffed lists. Once we handle the status and so the file, we just
    remove work assignment at index 0 of all lists. """

    deleted_or_sent = 0
    scuffed_files_SMA = []
    scuffed_files_DMA = []
    SMA_started = []
    DMA_started = []

    def __init__(self, folder_to_track, folder_destination, folder_documents, pool_hybrid_analysis, async_returns_hybridSMA, async_returns_hybridDMA):
        self.folder_to_track = folder_to_track
        self.folder_destination = folder_destination
        self.folder_documents = folder_documents
        self.pool_hybrid_analysis = pool_hybrid_analysis
        self.async_returns_hybridSMA = async_returns_hybridSMA
        self.async_returns_hybridDMA = async_returns_hybridDMA
        xprint()
        print("A new watchdog is awake !\r")
        print("Looking for suspicious files on : %s...\r" % folder_to_track)

    def on_modified(self, event):
        """ This function run itself when the folder/subfolder/file in folder is moved in/ modified"""
        if os.path.isdir(self.folder_to_track):
            for filename in os.listdir(self.folder_to_track):
                i = 1
                #dontcare, extension = os.path.splitext(filename)
                if filename != self.folder_to_track and filename != 'System Volume Information' and '.skp' != \
                        os.path.splitext(filename)[1] and os.path.splitext(filename)[1] in extensions.untrusted_extensions:

                    new_name = filename
                    xprint('swapping')
                    print("New suspect file is scuffed : " + new_name)

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
                            print("Too many files like this")
                            break

                    self.scuffed_files_SMA.append(filename)
                    self.scuffed_files_SMA.append(new_name)
                    print(" List of current scuffed files : ")
                    j = 0
                    for scuff in self.scuffed_files_SMA:
                        if j == 0:
                            print(scuff, end='-')
                        elif j % 2 == 0:
                            print(scuff, end='-')
                    print("\r")

                    quanrtineHandler.encrypt(self.folder_to_track, filename)
                    src = self.folder_to_track + "/" + filename
                    dst = self.folder_destination + "/" + new_name

                    shutil.move(src, dst)
                    #shutil.move(r"E:\\fgdg.txt", r"C:\users\julie\Desktop\fgdg2.txt") -> yes
                    time.sleep(0.05)

                    """ SENDING FOR SMA"""
                    self.async_returns_hybridSMA.append(self.pool_hybrid_analysis.apply_async(server.execute_analysis, (
                                "quick_scan_file", None, new_name)))
                    print("Your file has been sent for SMA and DMA. You'll get it back in /Documents/ once checked.\r")


        else:
            print("Watchdog CAN'T see the folder to track anymore! \r")
            self.on_deleted(event)

    def on_deleted(self, event):

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
        """ WE INCREMENT FILENAME LOCALLY. To avoid getting sames encryption keys
         when we encrypt again the same file! """
        """print(" A new download just finished ! ")
        if os.path.isdir(self.folder_to_track):
            for filename in os.listdir(self.folder_to_track):
                name, extension = os.path.splitext(filename)
                print("name %s" % name)
                print("extension %s", extension)

                if filename != self.folder_to_track and filename != 'System Volume Information' and '.skp' != extension and extension in extensions.untrusted_extensions:
                    i = 1
                    while filename + '.skp' in os.listdir(self.folder_to_track):
                        print("fiilename : %s" %filename)
                        new_name = name
                        if i > 2:
                            new_name = new_name[:-3]
                        new_name = new_name + extension
                        print("new_name : %s" % new_name)
                        os.rename(filename, new_name + '(' + str(i) + ')')
                        i += 1"""

    def on_removed(self):
        if len(self.folder_to_track) < 5 and not os.path.isdir(self.folder_to_track):
            xprint('swapping')
            print("A flashdrive device was REMOVED !")
            print("Killing watchdog over flashdrive...")
            sys.exit()

    def SMA(self):
        """try:
            print("len des reponses: ", len(self.async_returns_hybridSMA))
            print("status du premier elem: ", self.async_returns_hybridSMA[0])
            print("HandleSuspicious.SMA_started[0]: ", HandleSuspicious.SMA_started[0].ready())
            print("deleted or sent: ", HandleSuspicious.deleted_or_sent)
        except:
            print("toutes les conditions ne sont pas réunies")"""
        if len(self.async_returns_hybridSMA) > 0 and self.async_returns_hybridSMA[0].ready() and self.scuffed_files_SMA[0]:
            keepquarantine = self.async_returns_hybridSMA[0].get()
            if keepquarantine == 0:
                if (self.scuffed_files_SMA[0])[-4:] == '.exe':
                    self.async_returns_hybridDMA.append(self.pool_hybrid_analysis.apply_async(server.execute_analysis, (
                            "sandbox_file", None, self.scuffed_files_SMA[1])))
                    self.scuffed_files_DMA.append(self.scuffed_files_SMA[0])
                    self.scuffed_files_DMA.append(self.scuffed_files_SMA[1])
                    print("Your file %s has been sent for DMA" % self.scuffed_files_SMA[0])
                    self.scuffed_files_SMA.remove(self.scuffed_files_SMA[0])
                    self.scuffed_files_SMA.remove(self.scuffed_files_SMA[0])
                else:
                    quanrtineHandler.decrypt(self.folder_to_track, self.scuffed_files_SMA[0], self.folder_documents)
                    os.remove(os.getcwd() + r"\\uploadServer\\" + self.scuffed_files_SMA[1])
                    print("Your file %s is a clear file !\r" % self.scuffed_files_SMA[0])
                    self.scuffed_files_SMA.remove(self.scuffed_files_SMA[0])
                    self.scuffed_files_SMA.remove(self.scuffed_files_SMA[0])

            else:
                if keepquarantine == 1:
                    xprint()
                    print("Your file %s has been revealed to be a Ransomware/Malware !\r" % self.scuffed_files_SMA[0])
                    os.remove(getdownloadfolder() + r"\\" + self.scuffed_files_SMA[0] + '.skp')
                    os.remove(os.getcwd() + r"\\encryption\quarantineKey_" + self.scuffed_files_SMA[0] + '.skk')
                    quanrtineHandler.encrypt(os.getcwd() + r"\\uploadServer\\", self.scuffed_files_SMA[1])
                    self.scuffed_files_SMA.remove(self.scuffed_files_SMA[0])
                    self.scuffed_files_SMA.remove(self.scuffed_files_SMA[0])

                else:
                    print("SMA status of your file %s can't be established" % self.scuffed_files_SMA[0])
                    """ if .exe call DMA"""
                    self.scuffed_files_SMA.remove(self.scuffed_files_SMA[0])
                    self.scuffed_files_SMA.remove(self.scuffed_files_SMA[0])

            self.async_returns_hybridSMA.remove(self.async_returns_hybridSMA[0])

    def DMA(self):
        if len(self.async_returns_hybridDMA) > 0 and self.async_returns_hybridDMA[0].ready() and self.scuffed_files_DMA[0]:
            keepquarantine = self.async_returns_hybridDMA[0].get()

            if keepquarantine == 0:
                print("Your file %s is a clear file says DMA !\r" % self.scuffed_files_DMA[0])
                os.remove(os.getcwd() + r"\\uploadServer\\" + self.scuffed_files_DMA[1])
                quanrtineHandler.decrypt(self.folder_to_track, self.scuffed_files_DMA[0],
                                         self.folder_documents)
                self.scuffed_files_DMA.remove(self.scuffed_files_DMA[0])
                self.scuffed_files_DMA.remove(self.scuffed_files_DMA[0])


            elif keepquarantine == 1:
                print("Your file %s turned to be a Ransomware/Malware !\r" % self.scuffed_files_DMA[0])
                os.remove(getdownloadfolder() + r"\\" + self.scuffed_files_DMA[0])
                os.remove(os.getcwd() + r"\\encryption\quarantineKey_" + self.scuffed_files_DMA[0] + '.skk')
                quanrtineHandler.encrypt(os.getcwd() + r"\\uploadServer\\", self.scuffed_files_DMA[1])
                self.scuffed_files_DMA.remove(self.scuffed_files_DMA[0])
                self.scuffed_files_DMA.remove(self.scuffed_files_DMA[0])

            else:
                print("DMA status can't be established")
                self.scuffed_files_DMA.remove(self.scuffed_files_DMA[0])
                self.scuffed_files_DMA.remove(self.scuffed_files_DMA[0])

            self.async_returns_hybridDMA.remove(self.async_returns_hybridDMA[0])


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
    async_returns_hybridSMA = []
    async_returns_hybridDMA = []
    event_handler = HandleSuspicious(folder_to_track, folder_destination, folder_documents, pool_hybrid_analysis, async_returns_hybridSMA, async_returns_hybridDMA)
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
            event_handler.DMA()
            print_count += 1
            if print_count % 5 == 0:
                print("Looking for suspicious files on : %s...\r" % folder_to_track)
                print_count = 0
    except KeyboardInterrupt:
        print("KBM Interruption from watchdog process.")
    observer.stop()
    observer.join()
    xprint('swapping')


""" GENERAL CODE """
if __name__ == '__main__':
    if len(sys.argv) > 2:
        start_observer(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Arguments missing ! \n")