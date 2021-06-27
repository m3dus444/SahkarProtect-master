""" This is the main function of  Sahkar Protect """

import os
import sys
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


if __name__ == "__main__":
    print('\n' * 40)
    canvas.display_loading(2)

    """ Checking configuration"""

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

    pool_suspicious_handler = ThreadPool(processes=4)
    pool_USB_handler = ThreadPool(processes=2)
    pool_test = ThreadPool(processes=2)

    folder_to_track = SuspiciousHandler.getdownloadfolder()
    folder_destination = os.getcwd() + r'\uploadServer'
    folder_documents = r'C:\users\\' + getSessionUser.getuser(0) + r'\Documents'
    folder_device = ''

    xprint()
    print("Ran by : ", getSessionUser.getuser(0))
    print("Documents folder loaded: ", folder_documents)
    print("Download folder loaded: ", folder_to_track)
    print("Server folder loaded: ", folder_destination)
    time.sleep(3)

    asyncnever_returns_Sus_Handler = pool_suspicious_handler.apply_async(
        SuspiciousHandler.start_observer, (folder_to_track, folder_destination, folder_documents))

    async_returns_USB_Handler = pool_USB_handler.apply_async(
        USBHandler.looking_for_flash_drive)

    # while not asyncnever_returns_Sus_Handler.ready() and not async_returns_USB_Handler.ready():
    while True:
        try:
            if async_returns_USB_Handler.ready():
                new_flashdrive = async_returns_USB_Handler.get()
                xprint()
                print("A new FLASH DRIVE has been plugged in :", new_flashdrive)

                """ This one below works properly. But it cannot stop itself when USB is plugged out """
                asyncnever_returns_Sus_Handler2 = pool_test.apply_async(
                    SuspiciousHandler.start_observer, (new_flashdrive, folder_destination, folder_documents))

                async_returns_USB_Handler = pool_USB_handler.apply_async(USBHandler.looking_for_flash_drive)

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
            time.sleep(1)
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