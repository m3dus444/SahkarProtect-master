import os
import time

import quanrtineHandler
import shutil
"""a = os.getcwd() + r'\configs'
config_folder = fr"{a}"
print(config_folder)"""
#import SuspiciousHandler

#a = os.getcwd() + r'\configs'
#a.encode('unicode_escape')
#print(a)

"""
print(config_folder)
print(os.path.isdir(config_folder))

print(config_folder)
print(os.path.isdir(config_folder))
"""
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
#raw_s = r'{}'.format(s)

#'C:\\Users\\julie\\PycharmProjects\\SahkarProtect-master\\app\\configs\\chrome_config.txt'
def to_raw(string):
    return fr"{string}"
import extensions


def increment(x):
    x.append(2)

a = [100]
print(isinstance(a, object))
increment(a)
print(a)
print(time.time())
print(str(time.localtime()[3]) + "h " + str(time.localtime()[4]) + "min " + str(time.localtime()[5]) + "sec ")

class teton():
    d = {
            "watchdog" : ["a", "b"],
            "scuffed files" : ["c", "d"],
            "SMA_files" : ["e", "f"],
            "DMA_files" : ["g", "h"],
            "cleared_files" : ["i", "j"]
        }
    def __init__(self, var):
        self.var = var
    def printer(self, mode):
        if mode == 1:
            print("yes")

a = [3,7,6,4,5,0,6,5]
name = " JULIEN "
x = teton(a)
x.var.append(4)
for time in x.var:
    print("\t" + str(time) + "\t")

print(isinstance(x, object))
x.printer(1)

for additional in x.d:
    print(additional + ":")
    for info in x.d[additional]:
        print(info  +"\r")
print(a)
addinfo = []
#addinfo.append(eval(print(("The nameis so : ", name))))
print(addinfo)

addinfo.append(eval(r"str('The letter %s is a beautiful watchdog ! \n' %x.d['watchdog'][0])"))
#val("The name %s is a beautiful name ! %name")
print(2)
print(addinfo[0])
if x.printer(1):
    print("nooo")


kk = r"E:\\"
print(format(kk, ))

#dir2 = r'C:\Users\julie\Desktop\fgdg2.txt'
#dir = r'E:\\'
#time.sleep(5)
#print(os.path.isdir(dir))
#print(os.listdir(dir))
#open(r'C:\users\julie\Desktop\fgdg.txt', 'x')
#with open(r'E:\\fgdg.txt', 'r+') as file:
    #file.write("test")
#os.replace(r"E:\\fgdg.txt",r"C:\users\julie\Desktop\fgdg2.txt") -> no
#shutil.copy(r"E:\\fgdg.txt", r"C:\users\julie\Desktop\fgdg2.txt") -> yes
#shutil.move(r"E:\\fgdg.txt", r"C:\users\julie\Desktop\fgdg2.txt") -> yes
#os.remove(r"E:\\fgdg.txt") -> yes
#quanrtineHandler.encrypt(dir, 'fgdg.txt', 'fgdg.txt') -> yes
#quanrtineHandler.decrypt(dir, 'fgdg.txt', dir)
"""print("Owner id of the file:", os.stat(dir2).st_uid)
print("Group id of the file:", os.stat(dir2).st_gid)"""


#regarder pk l'observer se lance pas avec la clef USB



"""with open(os.getcwd() + r'\configs\testsss.txt', 'r+') as xprintcount:
    xprintcount.write("1")
with open(os.getcwd() + r'\configs\testsss.txt', 'r+') as xprintcount:
    xprintcount.write("2")
with open(os.getcwd() + r'\configs\testsss.txt', 'r') as xprintcount:
    print(xprintcount.readline(1))"""

"""canvas.display_loading(5)
time.sleep(3)


for i in range(10):
    xprint()
    print("new i : ", i)
#print(eval(a))"""


r"""
"""

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
"""

#proc = mp.Process(target = print_mynumber, args = (foo, ))#cannot target file.py even if we import it
#proc.start()
#subprocess.call(".\white.py", shell=True) #returns list index out of ranges of args

#function()
"""
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
r"""

r"C:Users\julie\PycharmProjects\SahkarProtect-masterapp\encryption"



old_string = "MK-36-W-357_IJO-36_3"
#k = old_string.rfind("_")
new_string = old_string[:old_string.rfind("_")] + "." + old_string[old_string.rfind("_")+1:].replace(str(3), str(4))
#new_string = old_string[:k] + old_string[k+1:].replace(str(3), str(4))
#os.system("cleandesk.py")
#exec(open("cleandesk.py").read())
print(os.getcwd())


def progressBar(current, total, barLength = 20):
    percent = float(current) * 100 / total
    arrow   = '-' * int(percent/100 * barLength - 1) + '>'
    spaces  = ' ' * (barLength - len(arrow))

    print('Progress: [%s%s] %d %%' % (arrow, spaces, percent), end='\r')

"""