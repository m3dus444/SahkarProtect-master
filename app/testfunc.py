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
import confHandler


class A(object):
    def __init__(self, x, b):
        _x = ''
        _b = 0
        self.y = _x
        self.z = _b
        print("ta mere je suis" + _x + " et j'ai " + str(_b))

    def method_a(self, foo, t):
        print(" mon pote est " + foo + "he as " + str(self.z) + "enfants")
        #print(self.)

a = A('test', 21) # We do not pass any argument to the __init__ method
#a.method_a('Sailor!', 22)
a.method_a('sailor', 22)

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