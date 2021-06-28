import os
from cryptography.fernet import Fernet


def encrypt(root, filename, incremented_filename):
    """ This function encrypt the file creating the quarantine  key
    in encryption folder. Then it encrypts the file in download folder
    with '.skp' extension as SuspiciousHandler will not scuff it. """

    root = root + r'\\'

    #  setting up the key used for encryption and decryption

    quarantine_key = Fernet.generate_key()

    with open(encryption_folder + 'quarantineKey_' + incremented_filename + '.skk', 'wb') as key:
        key.write(quarantine_key)

    f = Fernet(quarantine_key)  # creating fernet object

    #  encryption

    with open(root + filename, 'rb') as uncrypted_file:
        original_data = uncrypted_file.read()  # uncrypted data stored in RAM

    encrypted = f.encrypt(original_data)  # encrypted data of the file as a string stored in RAM for now
    del original_data

    with open(root + incremented_filename + '.skp', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)  # string is now written
        del encrypted


def decrypt(root, filename, incremented_filename, dst):
    """ This function decrypt the file reading the quarantine key written
        in encryption folder and removes both key and encrypted file"""

    root = root + '\\'
    dst = dst + '\\'

    with open(encryption_folder + 'quarantineKey_' + incremented_filename + '.skk', 'rb') as key:
        quarantine_key = key.read()
        f = Fernet(quarantine_key)

    with open(root + filename + '.skp', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open(dst + filename, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

    #  removing temp files
    os.remove(encryption_folder + 'quarantineKey_' + incremented_filename + '.skk')
    os.remove(root + filename + '.skp')


""" Local Variables """
encryption_folder = os.getcwd() + r"\encryption" + '\\'
