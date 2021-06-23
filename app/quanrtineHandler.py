import os
from cryptography.fernet import Fernet
import time

def encrypt(root, filename): #, extensionfile):

    root = root + r'\\'
    config_folder = os.getcwd() + r"\encryption" + '\\'

    """ setting up the key used for encryption and decryption"""

    quarantineKey = Fernet.generate_key()

    with open(config_folder + 'quarantineKey_' + filename + '.skk', 'wb') as key:
        key.write(quarantineKey)

    #with open('mykey.quarantineKey', 'rb') as key:
    #    quarantineKey = key.read()
    f = Fernet(quarantineKey) # creating fernet object

    """ encryption """

    with open(root + filename, 'rb') as uncrypted_file:
        original_data = uncrypted_file.read()  # uncrypted data stored in RAM

    encrypted = f.encrypt(original_data)  # encrypted data of the file as a string stored in RAM for now
    del original_data

    with open(root + filename + '.skp', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)  # string is now written
        del encrypted


""" decrypt """


def decrypt(root, encrypted_filename):
    config_folder = os.getcwd() + r"\encryption"
    root = root + '\\'
    config_folder = config_folder + '\\'

    with open(config_folder + 'quarantineKey_' + encrypted_filename + '.skk', 'rb') as key:
        quarantineKey = key.read()
        f = Fernet(quarantineKey)

    with open(root + encrypted_filename + '.skp', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open(root + encrypted_filename, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

    os.remove(config_folder + 'quarantineKey_' + encrypted_filename + '.skk')
    os.remove(root + encrypted_filename + '.skp')


encry = r"C:\Users\julie\PycharmProjects\SahkarProtect-master\app\encryption"
filename_toencrypt = "program.exe"

"""
encrypt(encry, filename_toencrypt)
time.sleep(5)
decrypt(encry, filename_toencrypt)
"""