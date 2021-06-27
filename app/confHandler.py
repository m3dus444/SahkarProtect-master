import os
import dlDirHandler
import canvas
from canvas import xprint as xprint


def set_chrome_config(value):
    try:
        with open(config_folder + r'\chrome_setup.txt', 'w') as configfile:
            configfile.write("chrome_entreprise_config = " + str(value) + ";")
            return True
    except:
        xprint()
        print("Cannot write configs files. Check chmod on : " + config_folder + " ...")
        return False


def is_chrome_configured():
    try:
        with open(config_folder + r'\chrome_setup.txt', 'r') as configfile:
            if '1' in configfile.read():
                return True
            else:
                return False
    except:
        xprint()
        print("Cannot read configs files. Trying to install missing files...")
        dlDirHandler.set_chrome_corp_mode()  # this will return False or True depending on called function and later
        # on set_chrome_config.


def set_regedit_config(value):
    try:
        with open(config_folder + r'\regedit_setup.txt', 'w') as configfile:
            configfile.write("regedit_policies_config = " + str(value) + ";")
            return True
    except:
        xprint()
        print("Cannot write configs files. Check chmod on : " + config_folder + " ...")
        return False


def is_regedit_configured():
    try:
        with open(config_folder + r'\regedit_setup.txt', 'r') as configfile:
            if '1' in configfile.read():
                return True
            else:
                return False
    except:
        # this will return False or True depending on called function and later on set_reg_config
        xprint()
        print("Cannot read configs files. Trying to install missing files...")
        dlDirHandler.set_chrome_reg_keys()


def set_guinea_pig_config():
    try:
        with open(config_folder + r'\guinea_pig.txt', 'w') as configfile:
            xprint()
            print("Successfully created guinea pig file")
            configfile.close()
        return True
    except:
        xprint()
        print("cannot write configs files. Check chmod on : " + config_folder + "...")
        return False


def to_raw(string):
    return fr"{string}"


""" Local variables """

config_folder = os.getcwd() + r"\configs"