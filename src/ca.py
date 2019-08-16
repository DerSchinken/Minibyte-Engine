# Check (Collision with a wall or something else)
import time
from src import mnlp


def move(pos, r, lvl):
    if r == 'l':
        if lvl[pos-1] == 1:
            pass
        elif lvl[pos-1] == 0:
            print('Gewonnen!')
            print('Exiting..')
            time.sleep(3)
            exit()
        else:
            lvl[pos] = 3
            lvl[pos-1] = 2
    if r == 'r':
        if lvl[pos+1] == 1:
            pass
        elif lvl[pos+1] == 0:
            print('Gewonnen!')
            print('Exiting..')
            time.sleep(3)
            exit()
        else:
            lvl[pos] = 3
            lvl[pos+1] = 2
    if r == 'd':
        opp = mnlp.gtopp()
        opp += 1
        if lvl[pos+opp] == 1:
            pass
        elif lvl[pos+opp] == 0:
            print('Gewonnen')
            print('Exitting..')
            time.sleep(3)
            exit()
        else:
            lvl[pos] = 3
            lvl[pos+opp] = 2
    if r == 'u':
        opp = mnlp.gtopp()
        opp += 1
        if lvl[pos-opp] == 1:
            pass
        elif lvl[pos-opp] == 0:
            print('Gewonnen')
            print('Exitting..')
            time.sleep(3)
            exit()
        else:
            lvl[pos] = 3
            lvl[pos-opp] = 2
    return lvl
