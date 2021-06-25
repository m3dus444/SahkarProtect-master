import os
import dlDirHandler


def set_chrome_config(value):
    try:
        with open(config_folder + 'chrome_setup.txt', 'w', encoding='utf-8') as configfile:
            configfile.write("chrome_entreprise_config = " + str(value) + ";")
            return True
    except:
        print("cannot write configs files. Check chmod on : " + config_folder + " ...")
        return False


def is_chrome_configured():
    print("config", config_folder)
    try:
        with open(config_folder + 'chrome_setup.txt', 'r', encoding='utf-8') as configfile:
            if '1' in configfile.read():
                return True
            else:
                return False
    except:
        print("cannot read configs files. Trying to install missing files...")
        dlDirHandler.set_chrome_corp_mode()  # this will return False or True depending on called function and later
                                             # on set_chrome_config.


def set_regedit_config(value):
    try:
        with open(config_folder + 'regedit_setup.txt', 'w', encoding='utf-8') as configfile:
            configfile.write("regedit_policies_config = " + str(value) + ";")
            return True
    except:
        print("cannot write configs files. Check chmod on : " + config_folder + " ...")
        return False


def is_regedit_configured():
    try:
        with open(config_folder + 'regedit_setup.txt', 'r', encoding='utf-8') as configfile:
            if '1' in configfile.read():
                return True
            else:
                return False
    except:
        # this will return False or True depending on called function and later on set_chrome_config
        print("cannot read configs files. Trying to install missing files...")
        dlDirHandler.set_chrome_reg_keys()


def set_guinea_pig_config():
    try:
        with open(config_folder + 'guinea_pig.txt', 'w') as configfile:
            print("Successfully created guinea pig file")
        return True
    except:
        print("cannot write configs files. Check chmod on : " + config_folder + " ...")
        return False


""" Local variables """

config_folder = os.getcwd() + r"\configs" + '\\'
