"""

This script returns the owner of the file, to get current session user name
As we run the script as administrator, the os.getuser will return Administrator
We want the session user name opened to add correct path in registry dir for dlDirHandler.py


"""

import win32api
import win32con
import win32security
import os
import getpass
import confHandler


def getuser(details):
    if os.path.isfile(os.getcwd() + r"\configs\guinea_pig.txt"):
        guinea_pig = os.getcwd() + r"\configs\guinea_pig.txt"
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
            print(getuser(details))
        else:
            print("You're probably ran this script in administrator mode. Try to run this script is user mode.")

if __name__ == '__main__':
    getuser(0)