import os
import pickle
import os.path
from posixpath import splitext
import time
from datetime import datetime
import socket


def log_init(filename):
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    stats = os.stat("./uploadServer/" + filename)

    d = {"ip address": local_ip, "nom": filename, "taille": stats.st_size, "date de creation": time.ctime(
        stats.st_ctime), "date de modification": time.ctime(stats.st_mtime)}

    with open("./logs/sakharlog.txt", "a") as f:
        dat = datetime.now()
        info = str(d)
        f.write(str(dat) + info + "\n")


def log_analysed(filename, result):
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    stats = os.stat("./uploadServer/" + filename)

    d = {"ip address": local_ip, "nom": filename, "result": result}

    with open("./logs/sakharlog.txt", "a") as f:
        dat = datetime.now()
        info = str(d)
        f.write(str(dat) + info + "\n")
