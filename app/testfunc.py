import ctypes
import subprocess
import sys
import os
import shutil
import time
from elevate import elevate
import win32api
import win32con
import win32security
import getSessionUser


if sys.version[0] == '2':
    input = raw_input
    import _winreg as wreg
else:
    import winreg as wreg

username = getSessionUser.getuser()  # replace all os.getLogin() by username
try:
    try:
        key = wreg.OpenKey(wreg.HKEY_LOCAL_MACHINE, "Software\\Policies\\Google\\Chrome", 0, wreg.KEY_ALL_ACCESS)
    except:
        key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "Software\\Policies\\Google\\Chrome")

    try:
        wreg.QueryValueEx(key, 'DefaultDownloadDirectory')
    except:
        wreg.SetValueEx(key, 'DefaultDownloadDirectory', 0, wreg.REG_SZ, 'c:\\users\\' + username +
                        '\\Downloads')

    try:
        wreg.QueryValueEx(key, 'DownloadDirectory')
    except:
        wreg.SetValueEx(key, 'DownloadDirectory', 0, wreg.REG_SZ, 'c:\\users\\' + username +
                        '\\Downloads')

    print(" *** KEYS SUCCESSFULLY ADDED TO REGISTRY ***")
    print(wreg.QueryValueEx(key, 'DefaultDownloadDirectory'))
    print(wreg.QueryValueEx(key, 'DownloadDirectory'))

    key.Close()

except:
    print(r"/!\ Couldn't access or modify registry :( /!\ ")

"""

old_string = "MK-36-W-357_IJO-36_3"
#k = old_string.rfind("_")
new_string = old_string[:old_string.rfind("_")] + "." + old_string[old_string.rfind("_")+1:].replace(str(3), str(4))
#new_string = old_string[:k] + old_string[k+1:].replace(str(3), str(4))
#os.system("cleandesk.py")
#exec(open("cleandesk.py").read())
print(os.getcwd())

"""
