import os
import sys
import time
import subprocess


def runcommand(commande):
    os.system('cmd /k ' + commande)
    #subprocess.run(commande, capture_output=True, text=True)
    try:
        while True:
            time.sleep(0.5)
            return 0
    except KeyboardInterrupt:
        return 1