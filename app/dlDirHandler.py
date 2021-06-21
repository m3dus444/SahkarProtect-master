"""

This script write in registry permanent Download destination folder
It will handle Mails Downloads later [WIP]


"""


import ctypes
import subprocess
import sys
import os
import getSessionUser

""" We check if we're on high privilege mode """

if os.name == 'nt':
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print('\nThis script requires to be ran with admin privileges\n')
        sys.exit()

""" For python 2"""

if sys.version[0] == '2':
    input = raw_input
    import _winreg as wreg
else:
    import winreg as wreg


""" Setting corp policies to chrome 
     We'll copy and past policies files to chrome dir and windows policies """

chrome_config_folder = os.getcwd() + r"\configs\chrome_entreprise_policies"
policy_definition_folder = r'C:\Windows\PolicyDefinitions'
supported_languages = ['fr-FR', 'fr', 'en-GB', 'en-US']

for root, languages, policies in os.walk(chrome_config_folder):

    # root = path to a policy | policies = list of all files in dir (and subdirs) | languages = list of all subdirs
    # lang = subdir for a language | lang_src/dst = path of lang |
    # Copying languages policies

    for lang in languages:
        if lang in supported_languages:
            lang_src = os.path.join(root, lang)
            lang_dst = os.path.join(policy_definition_folder, lang)

            if not os.path.isdir(policy_definition_folder + r"\\" + lang):
                os.mkdir(policy_definition_folder + r"\\" + lang)

            for policy_file in os.listdir(lang_src):
                os.popen("copy " + lang_src + r"\\" + policy_file + " " + lang_dst + r"\\" + policy_file)

    for policy in policies:
        if root == chrome_config_folder:  # root change every sub directories... so it'll be files from root path not subdirs
            # Do copy to win dir
            policy_src = os.path.join(root, policy)
            # policy dst is windows policy dir
            os.popen("copy " + policy_src + " " + policy_definition_folder + r"\\" + policy)


""" Creating keys 
    a wreg.openkey is generated after a wreg.createkey
    wreg.query can't be NULL as javascript query.
    If it fails, it drops an error and crash the pipe 
    So we have to handle bad request with tries
                                                    """

username = getSessionUser.getuser()  # replace all os.getLogin() by username
try:
    try:
        key = wreg.OpenKey(wreg.HKEY_LOCAL_MACHINE, "Software\\Policies\\Google\\Chrome", 0, wreg.KEY_ALL_ACCESS)
    except:
        key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "Software\\Policies\\Google\\Chrome")

    try:
        wreg.QueryValueEx(key, 'DefaultDownloadDirectory')
    except:
        wreg.SetValueEx(key, 'DefaultDownloadDirectory', 0, wreg.REG_SZ, 'c:\\users\\' + username +
                        '\\Downloads')

    try:
        wreg.QueryValueEx(key, 'DownloadDirectory')
    except:
        wreg.SetValueEx(key, 'DownloadDirectory', 0, wreg.REG_SZ, 'c:\\users\\' + username +
                        '\\Downloads')

    print(" *** KEYS SUCCESSFULLY ADDED TO REGISTRY ***")
    print("    ", wreg.QueryValueEx(key, 'DefaultDownloadDirectory'))
    print("    ", wreg.QueryValueEx(key, 'DownloadDirectory'))

    key.Close()

except:
    print(r"/!\ Couldn't access or modify registry :( /!\ ")


