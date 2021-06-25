import argparse
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
import json
import white
import subprocess
import multiprocessing as mp
#import SuspiciousHandler
from ctypes import windll
#from app import white
import concurrent.futures

"""
print('Total number of arguments:', format(len(sys.argv)))

# Print all arguments
print('Argument List:', str(sys.argv))

# Print arguments one by one
print('First argument:', str(sys.argv[0]))
print('Second argument:', str(sys.argv[1]))
print('Third argument:', str(sys.argv[2]))
print('Fourth argument:', str(sys.argv[3]))

parser = argparse.ArgumentParser(prefix_chars='-+/', description="This is to demonstrate multiple prefix characters")
parser.add_argument('multiply', type=int, help='Multiply a number by itself')
parser.add_argument('concat', type=str, help='concat str by itself')
#parser.add_argument("+a", "++add")
#parser.add_argument("-s", "--sub")
#parser.add_argument("/d", "//dir")
args = parser.parse_args()
print(args)
n = args.multiply
print(n * n)
c = args.concat
print(c + c)


"""
PYTHON_PATH = "D:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_5\python.exe"
ROOT = 'C:/Users/julie/PycharmProjects/SahkarProtect-master/app'
def function():
    PYTHON_PATH = "D:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_5\python.exe"
    ROOT = 'C:/Users/julie/PycharmProjects/SahkarProtect-master/app'
    cmd = r'"D:/Program Files (x86)/Microsoft Visual Studio/Shared/Python39_5/python.exe" C:/Users/julie/PycharmProjects/SahkarProtect-master/app/SuspiciousHandlerAlone.py ' + r'C:\Users\julie\Downloads C:\Users\julie\PycharmProjects\SahkarProtect-master\app\uploadServer'
    cmd = cmd.replace("/", "\\")
    print(cmd)
    #result = os.popen(cmd) #returns hexa status of cmd useless
    result = subprocess.run(cmd, capture_output=True, text=True) #returns 0 with args in cmd. Args passed but no returns value (0 ) getting stdout
    #result = subprocess.check_output([cmd, '2'], shell=True) #without printing or with, subprocess.CalledProcessError: Command returns non 0 exit value 1
    print(result)
    #py2output = subprocess.check_output([PYTHON_PATH, 'white.py', '2'])
    #stdout = result.stdout
    #stderr = result.stderr
    #print(py2output)
    #print(stdout)
   # print(stderr)
    #verdict = json.loads(stdout, strict=False)["verdict"]
    #return verdict
#function()


b = []
#b.append("True")
#b.append(None)
if b:
    print("OK")
print(len(b))


#CMD = r'"D:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_5\python.exe" C:/Users/julie/PycharmProjects/SahkarProtect-master/app/SuspiciousHandlerAlone.py C:\Users\julie\PycharmProjects\SahkarProtect-master\\app\\thrTestDir C:\Users\julie\PycharmProjects\SahkarProtect-master\\app\\testDir'

#print(os.system('cmd /k ' + CMD))




"""
from subprocess import Popen, PIPE

p = Popen([PYTHON_PATH, "white.py", "2"], stdin=PIPE, stdout=PIPE)
#input = "search Wrecking Ball\n" + "play 1\n"
output = p.communicate()[0]
print(output)
#output = b'' if no printing and = b'returnvalue\n\r' with printing

"""


"""
SUBPROCESSES:

# runSript.runcommand(createCMD(new_flashdrive))#can't continue code
# pool_test.apply_async(runSript.runcommand, createCMD(new_flashdrive)) # can't open observer
# subprocess.run(runSript.runcommand(createCMD(new_flashdrive)), capture_output=True, text=True)#can't continue code
# os.system('cmd /k ' + createCMD(new_flashdrive)) #can't continue code
# pool_test.apply_async(os.system, 'cmd /k ' + createCMD(new_flashdrive)) #can't open observer
# os.popen(createCMD(new_flashdrive)) # returns invalid arg ov argv lmao
# subprocess.run("os.system('cmd /k '" + createCMD(new_flashdrive), capture_output=False, text=True) #fichier specifie introuvable (lequel ? )


parser = argparse.ArgumentParser(prefix_chars='-+/', description="This is to demonstrate multiple prefix characters")
parser.add_argument("+a", "++add")
parser.add_argument("-s", "--sub")
parser.add_argument("/d", "//dir")
args = parser.parse_args()
print(args)
print(type(args))

"""

#proc = mp.Process(target = print_mynumber, args = (foo, ))#cannot target file.py even if we import it
#proc.start()
#subprocess.call(".\white.py", shell=True) #returns list index out of ranges of args

#function()
"""
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
"""

r"C:Users\julie\PycharmProjects\SahkarProtect-masterapp\encryption"



old_string = "MK-36-W-357_IJO-36_3"
#k = old_string.rfind("_")
new_string = old_string[:old_string.rfind("_")] + "." + old_string[old_string.rfind("_")+1:].replace(str(3), str(4))
#new_string = old_string[:k] + old_string[k+1:].replace(str(3), str(4))
#os.system("cleandesk.py")
#exec(open("cleandesk.py").read())
print(os.getcwd())

"""