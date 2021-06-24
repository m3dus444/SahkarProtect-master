import os
import pickle
import os.path
from posixpath import splitext
import time
from datetime import datetime
import socket

#path=r'C:\Users\Utilisteur\Desktop\downtest'
#directory=os.listdir(path)
filename = r'C:\Users\Utilisteur\Desktop\Book12.xlsx'

#print(fich[-1])

def loger(filename):
    fich= filename.split("\\")
    name, ext = os.path.splitext(filename)
    *chemin, nom=splitext(filename)

#    chemin = path + "\\"  + filename
    stats = os.stat(filename)
#    ip = os.popen(r"ipconfig | findstr 'IPv4' ")
#    print(ip)
    d={"nom":fich[-1],"taille":stats.st_size, "date de creation": time.ctime(stats.st_ctime), "date de modification":time.ctime(stats.st_mtime), "type":ext}
    print(d)

    with open("sakharlog.txt","a") as f:
        dat= datetime.now()
        f.write(str(dat)+str(d)+"\n")
        f.close()
loger(filename)
