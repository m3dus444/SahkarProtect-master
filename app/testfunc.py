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
import time
from ctypes import windll
import quanrtineHandler
import USBHandler





"""

C:\\Users\julie\PycharmProjects\SahkarProtect-master\\app\encryption



old_string = "MK-36-W-357_IJO-36_3"
#k = old_string.rfind("_")
new_string = old_string[:old_string.rfind("_")] + "." + old_string[old_string.rfind("_")+1:].replace(str(3), str(4))
#new_string = old_string[:k] + old_string[k+1:].replace(str(3), str(4))
#os.system("cleandesk.py")
#exec(open("cleandesk.py").read())
print(os.getcwd())

"""