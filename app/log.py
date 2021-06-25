import os
import pickle
import os.path
from posixpath import splitext
import time
from datetime import datetime
import socket

#path=r'C:\Users\Utilisteur\Desktop\downtest'
#directory=os.listdir(path)
filename = r'C:\Users\Utilisteur\Desktop\downtest\ecocompare.jar'


#function which creates log right after download
def loger(filename):
    fich = filename.split("\\")
    name, ext = os.path.splitext(filename)
    *chemin, nom = splitext(filename)
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    stats = os.stat(filename)

    d = {"ip address": local_ip, "nom": fich[-1], "taille": stats.st_size, "date de creation": time.ctime(
        stats.st_ctime), "date de modification": time.ctime(stats.st_mtime), "type": ext}
    print(d)

    with open("sakharlog.txt", "a") as f:
        dat = datetime.now()
        info = str(d)
        f.write(str(dat)+info+"\n")
        f.close()

#function which creates log after analyse


def logeranalysed(filename, result):
    fich = filename.split("\\")
    name, ext = os.path.splitext(filename)
    *chemin, nom = splitext(filename)
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    stats = os.stat(filename)

    d = {"ip address": local_ip, "nom": fich[-1], "result": result}
    print(d)

    with open("sakharlog.txt", "a") as f:
        dat = datetime.now()
        info = str(d)
        f.write(str(dat)+info+"\n")
        f.close()

#calling both functions
#loger(filename)
#logeranalysed(filename, 1)


os.system("pause")
