""" This is the main function of  Sakhar Protect """

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
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def checking_configuration():
    chrome_configured_state = confHandler.is_chrome_configured()
    regedit_configured_state = confHandler.is_regedit_configured()
    configuration_tries = 0

    while not chrome_configured_state or not regedit_configured_state:
        if not dlDirHandler.administrator_privilege():
            print("[" + Fore.RED + Style.BRIGHT + "-" + Fore.RESET + Style.RESET_ALL +
                  "] At first start, this script requires to be ran with admin privileges !\t")
            sys.exit()
        else:
            chrome_configured_state = dlDirHandler.set_chrome_corp_mode()
            regedit_configured_state = dlDirHandler.set_chrome_reg_keys()
            configuration_tries += 1
            if configuration_tries == 3:
                print("[" + Fore.RED + Style.BRIGHT + "-" + Fore.RESET + Style.RESET_ALL +
                      "] Too many config tries, something's causing a bug.\t")
                sys.exit()
        time.sleep(2)

    del chrome_configured_state
    del regedit_configured_state
    del configuration_tries


def start_watchdog_over_flashdrive(async_returns_USB_Handler):
    new_flashdrive = async_returns_USB_Handler.get()
    sakharprinter.additional_information["Script information"].append(
        eval(r"str('A new FLASH DRIVE has been plugged in : %s' % new_flashdrive)"))

    async_flash_drives.append(pool_test.apply_async(
        SuspiciousHandler.start_observer, (new_flashdrive, folder_destination, folder_documents, sakharprinter)))


if __name__ == "__main__":

    print('\n' * 40)
    canvas.display_loading(2)
    print('\n' * 80)

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
    sakharprinter = canvas.xprinter(folder_destination, folder_documents, getSessionUser.getuser(0), time.localtime())


    """ LAUNCHING PROCESSES """

    asyncnever_returns_Sus_Handler = pool_suspicious_handler.apply_async(
        SuspiciousHandler.start_observer, (folder_to_track, folder_destination, folder_documents, sakharprinter))

    async_returns_USB_Handler = pool_USB_handler.apply_async(
        USBHandler.looking_for_flash_drive)

    """ MAIN LOOP """

    while True:
        try:
            """ CHECKING FLASHDRIVE """
            if async_returns_USB_Handler.ready():
                start_watchdog_over_flashdrive(async_returns_USB_Handler)
                async_returns_USB_Handler = pool_USB_handler.apply_async(USBHandler.looking_for_flash_drive)
            if len(async_flash_drives) > 0:
                if async_flash_drives[0].ready:  # this means flash drives was removed
                    sakharprinter.additional_information["Awaken watchdogs"].remove(async_flash_drives[0].get())
                    async_flash_drives.remove(async_flash_drives[0])
                    sakharprinter.xprinting('swapping')

        except KeyboardInterrupt:
            pool_USB_handler.terminate()
            pool_suspicious_handler.terminate()
            del pool_USB_handler
            del pool_suspicious_handler
            del pool_test
            sakharprinter.xprint('swapping')
            print("Thanks for using our solution. See you soon.")
            print("Process will terminate itself give us a moment...")
            time.sleep(2)
            print("Done.")
            """time.sleep(0.65)
            sakharprinter.display_ending()"""
            break