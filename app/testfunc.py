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
import subprocess
import multiprocessing as mp
from ctypes import windll
from app import white

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
def function():
    PYTHON_PATH = "D:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_5\python.exe"
    ROOT = 'C:/Users/julie/PycharmProjects/SahkarProtect-master/app'
    cmd = r'"D:/Program Files (x86)/Microsoft Visual Studio/Shared/Python39_5/python.exe" C:/Users/julie/PycharmProjects/SahkarProtect-master/app/white.py'
    cmd = cmd.replace("/", "\\")
    print(cmd)
    result = os.popen(cmd)
    #result = subprocess.run(cmd, capture_output=True, text=True)
    #result = subprocess.check_output([cmd, '2'], shell=True)
    print(result)
    #py2output = subprocess.check_output([PYTHON_PATH, 'white.py', '2'])
    #stdout = result.stdout
    #stderr = result.stderr
    #print(py2output)
    #print(stdout)
   # print(stderr)
    #verdict = json.loads(stdout, strict=False)["verdict"]
    #return verdict


function()

"""
from subprocess import Popen, PIPE

p = Popen(["python", "respotify.py", "john", "doe"], stdin=PIPE, stdout=PIPE)
input = "search Wrecking Ball\n" + "play 1\n"
output = p.communicate(input)[0]



parser = argparse.ArgumentParser(prefix_chars='-+/', description="This is to demonstrate multiple prefix characters")
parser.add_argument("+a", "++add")
parser.add_argument("-s", "--sub")
parser.add_argument("/d", "//dir")
args = parser.parse_args()
print(args)
print(type(args))

"""

#proc = mp.Process(target = print_mynumber, args = (foo, ))
#proc.start()
#subprocess.call(".\white.py", shell=True)

#function()



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