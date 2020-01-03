# Mainloop to run the Game

import time
import os
import sys
from src import dspl, mmnt, mbki


lvl_gtopp = []
i = 0


def init(lvl):
    global lvl_gtopp

    _lvl = len(lvl[0])

    for i in range(len(lvl)):
        if len(lvl[i]) == _lvl:
            pass
        else:
            print('Du musst eine gerade und gleiche anzahl von zeichen haben')
            print('Exitting...')
            time.sleep(3)
            exit()

    lvl_gtopp = lvl

    lvl = dspl.init(lvl)
    return lvl


def gtopp():
    global lvl_gtopp
    return len(lvl_gtopp[0])


def start(lvl, ki=False, lives=6, delay=0.2):
    mlives = 4
    if not ki:
        lvl = init(lvl)
        while True:
            try:
                # This code is by Tornax07 thanks to him
                # For Windows
                if sys.platform == "win32":
                    os.system('cls')
                # For Linux
                else:
                    os.system('clear')
                if lives == 0:
                    print("Game Over")
                    exit()
                dspl.display_lvl(lvl, lives)
                lvl, lives, mlives = mmnt.mv(lvl, lives, mlives)
                time.sleep(delay)
            except KeyboardInterrupt:
                print('Exiting ')
                time.sleep(3)
                break
    else:
        try:
            mbki.MBKI(lvl, lives)
        except KeyboardInterrupt:
            print("Exiting ...")
            exit()
