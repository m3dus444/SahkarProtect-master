""" This is the main function of  Sahkar Protect """

import os
import sys
#sys.path.insert(0,'C:/Users/julie/PycharmProjects/SahkarProtect-master/app')
import time
from multiprocessing.pool import ThreadPool
import SuspiciousHandler
import USBHandler
import confHandler
import dlDirHandler
import getSessionUser
import canvas
from canvas import xprint as xprint


def checking_configuration():
    chrome_configured_state = confHandler.is_chrome_configured()
    regedit_configured_state = confHandler.is_regedit_configured()
    configuration_tries = 0

    while not chrome_configured_state or not regedit_configured_state:
        if not dlDirHandler.administrator_privilege():
            xprint()
            print('At first start, this script requires to be ran with admin privileges')
            sys.exit()
        else:
            dlDirHandler.set_chrome_corp_mode()
            dlDirHandler.set_chrome_reg_keys()
            configuration_tries += 1
            if configuration_tries == 3:
                xprint()
                print("Too many config tries, something's causing a bug.")
                sys.exit()

    del chrome_configured_state
    del regedit_configured_state
    del configuration_tries


def start_watchdog_over_flashdrive(async_returns_USB_Handler):
    new_flashdrive = async_returns_USB_Handler.get()
    xprint()
    print("A new FLASH DRIVE has been plugged in :", new_flashdrive)

    """ This one below works properly. But it cannot stop itself when USB is plugged out """
    async_flash_drives.append(pool_test.apply_async(
        SuspiciousHandler.start_observer, (new_flashdrive, folder_destination, folder_documents)))


if __name__ == "__main__":
    print('\n' * 40)
    canvas.display_loading(2)

    """ Checking configuration"""

    checking_configuration()

    """ LOCAL VARIABLES """
    pool_suspicious_handler = ThreadPool(processes=4)
    pool_USB_handler = ThreadPool(processes=2)
    pool_test = ThreadPool(processes=2)
    async_flash_drives = []

    folder_to_track = SuspiciousHandler.getdownloadfolder()
    folder_destination = os.getcwd() + r'\uploadServer'
    folder_documents = r'C:\users\\' + getSessionUser.getuser(0) + r'\Documents'
    folder_device = ''

    """ SYS INFORMATION"""
    xprint()
    print(getSessionUser.getuser('--info'))
    print("Documents folder loaded: ", folder_documents)
    print("Download folder loaded: ", folder_to_track)
    print("Server folder loaded: ", folder_destination)
    print("Launching processes...")
    time.sleep(3)

    asyncnever_returns_Sus_Handler = pool_suspicious_handler.apply_async(
        SuspiciousHandler.start_observer, (folder_to_track, folder_destination, folder_documents))

    async_returns_USB_Handler = pool_USB_handler.apply_async(
        USBHandler.looking_for_flash_drive)

    while True:
        try:
            """ CHECKING FLASHDRIVE """
            if async_returns_USB_Handler.ready():
                start_watchdog_over_flashdrive(async_returns_USB_Handler)
                async_returns_USB_Handler = pool_USB_handler.apply_async(USBHandler.looking_for_flash_drive)
            if len(async_flash_drives) > 0:
                if async_flash_drives[0].ready:# this means flash drives was removed
                    async_flash_drives.remove(async_flash_drives[0])

        except KeyboardInterrupt:
            pool_USB_handler.terminate()
            pool_suspicious_handler.terminate()
            del pool_USB_handler
            del pool_suspicious_handler
            del pool_test
            xprint()
            print("Thanks for using our solution. See you soon.")
            print("Process will terminate itself give us a moment...")
            time.sleep(2)
            print("Done.")
            time.sleep(0.65)
            canvas.display_ending()
            break

""" LOCAL VARIABLES """



r"""pool_suspicious_handler = ThreadPool(processes=4)
pool_USB_handler = ThreadPool(processes=2)
pool_test = ThreadPool(processes=2)

folder_to_track = SuspiciousHandler.getdownloadfolder()
folder_destination = os.getcwd() + r'\uploadServer'
folder_documents = r'C:\users\\' + getSessionUser.getuser(0) + r'\Documents'
folder_device = ''
"""