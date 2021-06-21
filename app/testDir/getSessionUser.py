"""

This script returns the owner of the file, to get current session user name
As we run the script as administrator, the os.getuser will return Administrator
We want the session user name opened to add correct path in registry dir for dlDirHandler.py


"""

import win32api
import win32con
import win32security
import os

def getUser():
    basedir = r"C:/"  # i we need to do an os.path.join
    FILENAME = os.getcwd() + r"\extensions.py"
    open(FILENAME, "r").close()
    print( "This script is ran by : ", win32api.GetUserNameEx(win32con.NameSamCompatible))  # returns runner of the script
    security_description = win32security.GetFileSecurity(FILENAME, win32security.OWNER_SECURITY_INFORMATION)  # returns security file description
    owner_sid = security_description.GetSecurityDescriptorOwner()  # returns Owner sid from file sec description
    name, domain, type = win32security.LookupAccountSid(None, owner_sid)  # extract Owner name from sid

    print("File owned by %s\\%s" % (domain, name))
    return name


print(getUser())