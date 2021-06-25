""" This is the main function of  Sahkar Protect """

import confHandler
import dlDirHandler
import sys
from multiprocessing.pool import ThreadPool
import app.white
import time
from sys import getsizeof
import argparse
import ctypes
import subprocess
import sys
import os
import shutil
import win32api
import win32con
import win32security
import app.getSessionUser
import json
import app.USBHandler
import app.SuspiciousHandler
import app.runSript
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import quanrtineHandler
import server
from app import getSessionUser, SuspiciousHandler, USBHandler


def createCMD(target_dir):
    CMD = r'"D:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_5\python.exe" C:/Users/julie/PycharmProjects/SahkarProtect-master/app/SuspiciousHandlerAlone.py ' + \
        target_dir + r" C:\Users\julie\PycharmProjects\SahkarProtect-master\\app\\uploadServer"
    return CMD


"""class A(object):
    def __init__(self, something):
        print("A init called")
        self.something = something


class B(A):
    def __init__(self, something):
        # Calling init of parent class
        A.__init__(self, something)
        print("B init called")
        self.something = something"""

""" Checking configuration"""

print(getSessionUser.getuser('--info'))
time.sleep(1)
chrome_configured_state = confHandler.is_chrome_configured()
regedit_configured_state = confHandler.is_regedit_configured()
configuration_tries = 0

while not chrome_configured_state or not regedit_configured_state:
    dlDirHandler.set_chrome_corp_mode()
    dlDirHandler.set_chrome_reg_keys()
    configuration_tries += 1
    if configuration_tries == 3:
        print("Too many config tries, something's causing a bug.")
        sys.exit(__status="Too many configuration tries")

del chrome_configured_state
del regedit_configured_state
del configuration_tries

pool_suspicious_handler = ThreadPool(processes=4)
pool_USB_handler = ThreadPool(processes=2)
pool_test = ThreadPool(processes=2)

folder_to_track = SuspiciousHandler.getdownloadfolder()
folder_destination = os.getcwd() + r'\uploadServer'
folder_documents = r'C:\users\\' + getSessionUser.getuser(0) + r'\Documents'
folder_device = ''
#CMD = r'"D:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_5\python.exe" C:/Users/julie/PycharmProjects/SahkarProtect-master/app/SuspiciousHandlerAlone.py ' + folder_device + r" C:\Users\julie\PycharmProjects\SahkarProtect-master\\app\\uploadServer"

#download_watchdog = SuspiciousHandler.HandleSuspicious()
#SuspiciousHandler.start_observer(folder_to_track, folder_destination)

asyncnever_returns_Sus_Handler = pool_suspicious_handler.apply_async(
    SuspiciousHandler.start_observer, (folder_to_track, folder_destination, folder_documents))
#async_returns_USB_Handler = pool_suspicious_handler.apply_async(USBHandler.looking_for_flash_drive)
# pool_suspicious_handler.close()
async_returns_USB_Handler = pool_USB_handler.apply_async(
    USBHandler.looking_for_flash_drive)
# pool_USB_handler.close()

# while not asyncnever_returns_Sus_Handler.ready() and not async_returns_USB_Handler.ready():
while True:
    try:
        # print(async_returns_USB_Handler.ready())
        if async_returns_USB_Handler.ready():
            new_flashdrive = async_returns_USB_Handler.get()
            print(new_flashdrive)
            """ This one below works properly. But it cannot stop itself when USB is plugged out """
            asyncnever_returns_Sus_Handler2 = pool_test.apply_async(
                SuspiciousHandler.start_observer, (new_flashdrive, folder_destination, folder_documents))
            # time.sleep(0.5)
            print(createCMD(new_flashdrive))
            time.sleep(5)
            print("TEST PASSED")
            async_returns_USB_Handler = pool_USB_handler.apply_async(USBHandler.looking_for_flash_drive)
        time.sleep(3)

    except KeyboardInterrupt:
        pool_USB_handler.terminate()
        pool_suspicious_handler.terminate()
        break

del pool_USB_handler
del pool_USB_handler
