# Mainloop to run the Game

import time
import os
import sys
from src import dspl, mmnt, mbki, new_mbki


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


def getmaze(lvl, lvl_new=[]):
    if ' ' in lvl[0] or ' ' in lvl[len(lvl) - 1]:
        print(
            "Stell bitte sicher das dein Level überall an der seite\nränder (X) hat damit der Spieler nicht out off bounce gelangt\nund dort schaden(Glitches/Bugs) veruscachen kann!")
        exit()

    for i in range(len(lvl)):
        try:
            if lvl_new[len(lvl_new) - 1] == 3:
                print("Stell bitte sicher das dein Level überall an der seite\nränder (X) hat damit der Spieler nicht"
                      " out off bounce gelangt\nund dort schaden(Glitches/Bugs) veruscachen kann!")
                exit()
        except IndexError:
            print('')

        lvl_new.append([])
        for o in lvl[i]:
            if o == 'X':
                lvl_new[i].append(1)
            if o == 'P':
                lvl_new[i].append(0)
            if o == 'F':
                lvl_new[i].append(0)
            if o == ' ':
                lvl_new[i].append(0)
            if o == 'G':
                lvl_new[i].append(1)
    return lvl_new


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
            new_mbki.main(lvl, lives, mlives)
        except KeyboardInterrupt:
            print("Exiting ...")
            exit()
