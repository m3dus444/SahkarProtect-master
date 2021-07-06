import os
import time


class xprinter():
    additional_information = {
            "Awaken watchdogs": [],
            "Script information": [],
            "Scuffed files": [],
            "SMA files": [],
            "DMA files": [],
            "Analysed files": [],
            "Errors": [],
            "Others": []
        }
    working = 0

    def __init__(self, folder_destination, folder_document, user, date_run): #, additional_information):
        self.folder_destination = folder_destination
        self.folder_document = folder_document
        self.user = user
        self.date_run = date_run
        self.execdate = []
        self.execdate.append(date_run[3])
        self.execdate.append(date_run[4])
        self.execdate.append(date_run[5])

    def xprint(self, mode=None):
        time.sleep(0.1)
        if mode == 'swapping':
            display_swapping(1, 1.0)
            display_canvas(1)
        elif mode == 'jump':
            print('\n' * 20)
            display_canvas(1)

    def display_ending(self):
        display_swapping(2, 2.0)
        display_canvas(4)

    def xprinting(self, mode):
        if not self.working:
            mode = 'jump'
            self.working = 1
            self.xprint(mode)
            print("\tScript launched by:\t", self.user)
            print("\tAt : " + str(self.execdate[0]) + "h " + str(self.execdate[1]) + "min " + str(self.execdate[2]) + "sec \t")
            print("\tUploadServer location :\t", self.folder_destination)
            print("\tClear file location :\t", self.folder_document)
            print("\tAdditional informations :\n")
            for additional in self.additional_information:
                if len(self.additional_information[additional]):# != 0:
                    print("\t•" + additional + ":")
                    for info in self.additional_information[additional]:
                        print("\t\t" + info)
            self.working = 0
            self.del_script_info() #throw all information away after printing them
        else:
            time.sleep(0.1)
            self.xprinting(mode)
    def add_script_info(self, info):
        self.additional_information["Script information"].append(info)
    def del_script_info(self, info=None):
        if info is not None:
            self.additional_information["Script information"].remove(info)
        else:
            del self.additional_information["Script information"][:]
            del self.additional_information["Others"][:]
            del self.additional_information["Errors"][:]







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

"""def display_ending():
    display_swapping(2, 2.0)
    display_canvas(4)"""

class teee():
    x = []
    def __init__(self):
        print("init")

uuu = teee()

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
        #xprint()
        print(i)
        time.sleep(3)