""" In this script, we will reverse the bit algorithm that Windows
    uses to encode list of Uppercase letters of devices in a integer base 2.


    The encoded method is  :
    The lower case device is 1 in base 2, and for each letter in alphabet letters
    from lower case device to letter A ( the first one -.- ) we do a left shift.
    The encoded integer corresponding to the list of our device will be the one
    that the operation AND(last bit, 1) returns 1 every time the left shift current operation
    is done for a device we have.


    To do so, we loop for each uppercase and we do a right shift of bits
    and for each time, we check if the encoded integer AND 1 is true
    If so, it means the uppercase letter was encoded and therefore
    we have a device plugged in with this letter
    If it's false, we do an shift right to keep going.
    For example, if we have C:/ and D:/, current encoded int will be
    12 (1100), as we have to loop 4 times to lower the integer to 0:
    1st loop: 1100 --> 0110   ---> A
    2nd loop: 0110 --> 0011  ----> B
    3rd loop: 0011 --> 0001 ---> C
    4th loop: 0001 --> 0000 ---> D

    To do the AND operator, we take the last two bits. So for first loop
    aka letter A, it'll return 0, for letter B as well and C and D it returns 1. """


import os
import time
import getSessionUser
from ctypes import windll


def get_drive_status():
    devices = []
    record_deviceBit = windll.kernel32.GetLogicalDrives()  # The GetLogicalDrives function retrieves a bitmask for devices

    for label in uppercase_letters:
        """ We check if bitmask AND 1 returns 1 ==> both bits are 1"""

        if record_deviceBit & 1:
            devices.append(label) # if it is, we add the correspondant label

        """ If both bits arent 1"""
        record_deviceBit >>= 1
                                # the >> operator Shifts right by pushing copies of the leftmost bit in from the left,
                                # and lets the rightmost bits fall off
    return devices


def detect_flash_drive():

    original = set(get_drive_status())
    time.sleep(1)
    add_device = set(get_drive_status()) - original
    subt_device = original - set(get_drive_status())

    if len(add_device):
        print("There were %d" % (len(add_device)))
        for drive in add_device:
            print("The drives added: %s." % drive)
            return drive + r':\\'

    elif len(subt_device):
        print("There were %d" % (len(subt_device)))
        for drive in subt_device:
            print("The drives remove: %s." % drive)


def looking_for_flash_drive():
    i = 0
    time.sleep(5)  # we wait for other xprint to come first (watchdog's one)
    print('Looking for flashdrive...')
    new_device = False
    while not new_device:
        new_device = detect_flash_drive()
        i += 1
        if i % 10 == 0:
            print('Looking for flashdrive...')
    return new_device


""" Local Variabkes"""

uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']