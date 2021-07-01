import os
import time
import SuspiciousHandler

def xprint(mode):
    time.sleep(0.1)
    if mode == 'swapping':
        display_swapping(1, 1.0)
    elif mode == 'jump':
        print('\n' * 10)
    display_canvas(1)


class xprintt():
    additional_information = {}
    def __init__(self, folder_to_track, folder_destination, folder_document, user, date_run):
        self.folder_to_track = folder_to_track
        self.folder_destination = folder_destination
        self.folder_document = folder_document
        self.user = user
        self.date_run = date_run

    def xprinting(self, mode):
        xprint(mode)
        print("\tWatchdog over :\t", self.folder_to_track)
        print("\tUploadServer location: \t", self.folder_destination)
        print("\tClear file location:\t", self.folder_document)
        print("\tScript launched by:\t", self.user)
        print("\tAt:\t", self.date_run)





def xprinttest():
    if os.path.isfile(os.getcwd() + r'\configs\xprintcounter.txt'):
        with open(os.getcwd() + r'\configs\xprintcounter.txt', 'r+') as xprintcount:
            if int(xprintcount.readline(1)) >= 5:
                time.sleep(0.3)
                print('\n' * 10)
                display_canvas(1)
            else:
                xprintcount.write(str(int(xprintcount.readline(1)) + 1))
    else:
        f = open(os.getcwd() + r'\configs\xprintcounter.txt', 'x')
        with open(os.getcwd() + r'\configs\xprintcounter.txt', 'r+') as xprintcount:
            xprintcount.write("1")

def xprintloading():
    print('\n' * 40)
    display_canvas(1)

def display_canvas(canvas_index):
    for pencil in canvas_room[canvas_index]:
        print(pencil)
    print("\n")


def display_loading(counter):
    for i in range(counter):
        for load in canvas_room[2]:
            xprintloading()
            print(load)
            time.sleep(0.1)

def display_swapping(counter, speed):
    for i in range(counter):
        for spike in canvas_room[3]:
            print(spike)
            time.sleep(0.035 * 1 / speed)

def display_ending():
    display_swapping(2, 2.0)
    display_canvas(4)

canvas_room = [
    ["░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\r",
     "░░░      ░░░░░░░░░  ░░░░░░░░   ░░░░   ░   ░░░   ░░░░░░░░░  ░░░░░░░░        ░░░░\r",
     "▒   ▒▒▒▒   ▒▒▒▒▒▒  ▒  ▒▒▒▒▒▒   ▒▒▒▒   ▒   ▒▒   ▒▒▒▒▒▒▒▒▒  ▒  ▒▒▒▒▒▒   ▒▒▒▒   ▒▒\r",
     "▒▒   ▒▒▒▒▒▒▒▒▒▒▒  ▒▒   ▒▒▒▒▒   ▒▒▒▒   ▒   ▒   ▒▒▒▒▒▒▒▒▒  ▒▒   ▒▒▒▒▒   ▒▒▒▒   ▒▒\r",
     "▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓▓▓   ▓▓▓▓          ▓  ▓  ▓▓▓▓▓▓▓▓▓▓   ▓▓▓   ▓▓▓▓  ▓   ▓▓▓▓▓▓\r",
     "▓▓▓▓▓▓▓   ▓▓▓▓       ▓   ▓▓▓   ▓▓▓▓   ▓   ▓▓   ▓▓▓▓▓▓       ▓   ▓▓▓   ▓▓   ▓▓▓▓\r",
     "▓   ▓▓▓▓   ▓▓   ▓▓▓▓▓▓▓   ▓▓   ▓▓▓▓   ▓   ▓▓▓   ▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓   ▓▓▓▓   ▓▓\r",
     "███      ███   █████████   █   ████   █   █████   █   █████████   █   ██████   \r",
     "███████████████████████████████████████████████████████████████████████████████\r",
     ],
    ["  ██████  ▄▄▄      ▀██ ▄█▀  ██░ ██  ▄▄▄      ██▀███  \r",
     "▒██    ▒ ▒████▄     ██▄█▒ ▒▓██░ ██ ▒████▄   ▓██ ▒ ██▒\r",
     "░ ▓██▄   ▒██  ▀█▄  ▓███▄░ ░▒██▀▀██ ▒██  ▀█▄ ▓██ ░▄█ ▒\r",
     "  ▒   ██▒░██▄▄▄▄██ ▓██ █▄  ░▓█ ░██ ░██▄▄▄▄██▒██▀▀█▄  \r",
     "▒██████▒▒ ▓█   ▓██ ▒██▒ █▄ ░▓█▒░██▓ ▓█   ▓██░██▓ ▒██▒\r",
     "▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█ ▒ ▒▒ ▓▒  ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒▓ ░▒▓░\r",
     "░ ░▒  ░    ░   ▒▒  ░ ░▒ ▒░  ▒ ░▒░ ░  ░   ▒▒   ░▒ ░ ▒░\r",
     "░  ░  ░    ░   ▒   ░ ░░ ░   ░  ░░ ░  ░   ▒     ░   ░\r",
     "      ░        ░   ░  ░     ░  ░  ░      ░     ░     \r"
     ],
    [
        "                   ▄▄▄▄▄▄▄▄▄▄▄\r",
        "                   ▀▄▄▄▄▄▄▄▄▄▄\r",
        "                   ▄▀▄▄▄▄▄▄▄▄▄\r",
        "                   ▄▄▀▄▄▄▄▄▄▄▄\r",
        "                   ▄▄▄▀▄▄▄▄▄▄▄\r",
        "                   ▄▄▄▄▀▄▄▄▄▄▄\r",
        "                   ▄▄▄▄▄▀▄▄▄▄▄\r",
        "                   ▄▄▄▄▄▄▀▄▄▄▄\r",
        "                   ▄▄▄▄▄▄▄▀▄▄▄\r",
        "                   ▄▄▄▄▄▄▄▄▀▄▄\r",
        "                   ▄▄▄▄▄▄▄▄▄▀▄\r",
        "                   ▄▄▄▄▄▄▄▄▄▄▀\r",
        "                   ▄▄▄▄▄▄▄▄▄▄▄\r"

    ],
    ['                                   *',
     '                                        *',
     '                                            *',
     '                                               *',
     '                                                 *',
     '                                                 *',
     '                                               *',
     '                                            *',
     '                                       *',
     '                                *',
     '                          *',
     '                   *',
     '              *',
     '           *',
     '          *',
     '          *',
     '            *',
     '                 *',
     '                       *',
     '                             *'
     ],
    [
        "╔═══════════════════════════════════════════════════╗\r",
        "║ ▀██ ▄█▀  ██ ███▄    █    ▄████    ▄████    ▄████  ║\r",
        "║  ██▄█▒ ▒▓██ ██ ▀█   █ ▒ ██▒ ▀█▒▒ ██▒ ▀█▒▒ ██▒ ▀█▒ ║\r",
        "║ ▓███▄░ ░▒██▓██  ▀█ ██▒░▒██░▄▄▄░░▒██░▄▄▄░░▒██░▄▄▄░ ║\r",
        "║ ▓██ █▄  ░██▓██▒  ▐▌██▒░░▓█  ██▓░░▓█  ██▓░░▓█  ██▓ ║\r",
        "║ ▒██▒ █▄ ░██▒██░   ▓██░░▒▓███▀▒░░▒▓███▀▒░░▒▓███▀▒░ ║\r",
        "║ ▒ ▒▒ ▓▒ ░▓ ░ ▒░   ▒ ▒  ░▒   ▒   ░▒   ▒   ░▒   ▒   ║\r",
        "║ ░ ░▒ ▒░  ▒ ░ ░░   ░ ▒░  ░   ░    ░   ░    ░   ░   ║\r",
        "║ ░ ░░ ░   ▒    ░   ░ ░ ░ ░   ░ ░░ ░   ░ ░░ ░   ░ ░ ║\r",
        "║ ░  ░     ░          ░       ░     ░      ░       ░║\r",
        "╚═══════════════════════════════════════════════════╝\r"
    ],
]

if __name__ == '__main__':
    display_loading(5)
    for i in range(10):
        xprint()
        print(i)
        time.sleep(3)