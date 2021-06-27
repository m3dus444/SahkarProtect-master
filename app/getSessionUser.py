"""

This script returns the owner of the file, to get current session user name
As we run the script as administrator, the os.getuser will return Administrator
We want the session user name opened to add correct path in registry dir for dlDirHandler.py


"""
import sys
import time

import win32api
import win32con
import win32security
import confHandler
import os


def getuser(details):
    #if os.path.isfile(r'' + os.getcwd() + r"\configs\guinea_pig.txt"):
    if os.path.isfile(config_folder + r"\guinea_pig.txt"):
        #guinea_pig = r'' + os.getcwd() + r"\configs\guinea_pig.txt"
        guinea_pig = config_folder + r"\guinea_pig.txt"
        security_description = win32security.GetFileSecurity(guinea_pig, win32security.OWNER_SECURITY_INFORMATION)  # returns security file description
        owner_sid = security_description.GetSecurityDescriptorOwner()  # returns Owner sid from file sec description
        name, domain, type = win32security.LookupAccountSid(None, owner_sid)  # extract Owner name from sid

        # print("File owned by %s\\%s" % (domain, name))
        if details == 0:
            return name
        else:
            print("This script is ran by : ",
                  win32api.GetUserNameEx(win32con.NameSamCompatible))  # returns runner of the script
            print("** User logged in current Windows Session : ", name + " **")
            return name
    else:
        print("missing guinea pig file. Trying to create one...")
        if os.getlogin() in os.getcwd():
            confHandler.set_guinea_pig_config()
            print("Configs files generated, please restart script.")
            time.sleep(1)
            sys.exit()
        else:
            print("You're probably ran this script in administrator mode. Try to run this script is user mode.")


config_folder = os.getcwd() + r'\configs'
#config_folder = "C:\\Users\\julie\\PycharmProjects\\SahkarProtect-master\\app\\configs"
#config_folder_no_raw = os.getcwd() + '\\configs'
#config_folder = fr"{config_folder_no_raw}"
#config_folder.encode('unicode_escape')
#config_folder = confHandler.to_raw(os.getcwd() + r'\configs')

if __name__ == '__main__':
    print(getuser(0))