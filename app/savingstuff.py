#! /usr/bin/env python3

from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import json
import shutil


class HandleSuspicious(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'test':
                new_name = filename
                print("this is the filename : " + filename + '\n')
#                split_name = filename.split('.')
                file_exists = os.path.isfile(folder_destination + '/' + new_name)
                print("already a file ? : ", file_exists, '\n')
                while file_exists:
                    i += 1
                    #new_name = os.path.splitext(folder_to_track + '/' + new_name)[0] + str(i) + os.path.splitext(folder_to_track + '/' + new_name)[1]
                    if i > 2:
                        k = new_name.rfind("_")
                        new_name = new_name[:k] + "_" + new_name[k+1:].replace(str(i-1), str(i))
                    else:
                        #new_name = new_name + str(i)
                        new_name = os.path.splitext(new_name)[0] + "_" + str(i) + \
                                   os.path.splitext(new_name)[1]
                    print("this is the new name with a number !  : " + new_name + '\n')
#                    new_name = new_name.split("/")[4]
#                    print("this is the new name with the number after the split: " + new_name + '\n')
                    #new_name = new_name.replace(folder_to_track, folder_destination)
                    file_exists = os.path.isfile(folder_destination + "/" + new_name)
                    print("another file exists : ", file_exists, '\n')
                    if i >= 20:
                        break

                src = folder_to_track + "/" + filename
                print("this is the src name : " + src + '\n')
                #new_name = new_name.replace(folder_to_track, '')
                dst = folder_destination + "/" + new_name
                dst = dst.replace(folder_to_track, '')
                #dst = new_name
                print("this is the dst name : " + dst + '\n')
                #os.rename(src, dst)


folder_to_track = 'C:/users/julie/Desktop/watched'
folder_destination = 'C:/users/julie/Desktop/test'

event_handler = HandleSuspicious()
observer = Observer()
observer.schedule(event_handler, path=folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
