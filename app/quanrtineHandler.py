from cryptography.fernet import Fernet

""" setting up key for encryption and decryption"""
quarantineKey = Fernet.generate_key()

with open('mykey.quarantineKey', 'wb') as key:
    key.write(quarantineKey)

with open('mykey.quarantineKey', 'rb') as key:
    quarantineKey = key.read()

print(quarantineKey)

f = Fernet(quarantineKey)

filename = "file_to"

""" encrypt """

with open(filename + '_encrypt.txt', 'rb') as uncrypted_file:
    original = uncrypted_file.read()  # uncrypted data stored in RAM

encrypted = f.encrypt(original)  # encrypted data of the file as a string stored in RAM for now
del original
print("encrypted string : ", encrypted)

with open('encrypted_file_to_encrypt.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)  # string is now writed
    del encrypted

""" decrypt """

with open('encrypted_file_to_encrypt.txt', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)
print("decrypted string : ", decrypted)

with open('decrypted_file_to_encrypt.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)
