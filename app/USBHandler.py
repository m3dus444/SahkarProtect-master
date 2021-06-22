import os, string, time
from ctypes import windll

uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def get_driveStatus():
    devices = []
    record_deviceBit = windll.kernel32.GetLogicalDrives()  # The GetLogicalDrives function retrieves a bitmask
    # representing the currently available disk drives.
    for label in uppercase_letters:  # The uppercase letters 'A-Z'
        if record_deviceBit & 1:
            devices.append(label)
        record_deviceBit >>= 1
    return devices


def detect_device():
    original = set(get_driveStatus())
    print('Detecting...')
    time.sleep(3)
    add_device = set(get_driveStatus()) - original
    subt_device = original - set(get_driveStatus())

    if (len(add_device)):
        print("There were %d" % (len(add_device)))
        for drive in add_device:
            print("The drives added: %s." % (drive))

    elif (len(subt_device)):
        print("There were %d" % (len(subt_device)))
        for drive in subt_device:
            print("The drives remove: %s." % (drive))


if __name__ == '__main__':

    while True:
        detect_device()
