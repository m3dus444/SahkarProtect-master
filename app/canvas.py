import os
import time

def xprint():
    time.sleep(0.1)
    display_swapping(1, 1.0)
    #print('\n' * 10)
    display_canvas(1)


class xprintt():
    def __init__(self):
        xprint()
        # do stuff

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