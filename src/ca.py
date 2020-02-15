# Check (Collision with a wall or something else)
import time
from src import mnlp


def move(pos, r, lvl, lives, mlives):
    if r == 'l':
        if lvl[pos-1] == 1:
            pass
        elif lvl[pos-1] == 0:
            print('Gewonnen!')
            print('Exiting..')
            time.sleep(3)
            exit()
        elif lvl[pos-1] == 5:
            if not mlives == 0:
                lives -= 1
                mlives -= 1
            else:
                lvl[pos] = 3
                lvl[pos-1] = 2
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
        elif lvl[pos+1] == 5:
            if not mlives == 0:
                lives -= 1
                mlives -= 1
            else:
                lvl[pos] = 3
                lvl[pos+1] = 2
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
        elif lvl[pos+opp] == 5:
            if not mlives == 0:
                lives -= 1
                mlives -= 1
            else:
                lvl[pos] = 3
                lvl[pos+opp] = 2
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
        elif lvl[pos-opp] == 5:
            if not mlives == 0:
                lives -= 1
                mlives -= 1
            else:
                lvl[pos] = 3
                lvl[pos-opp] = 2
        else:
            lvl[pos] = 3
            lvl[pos-opp] = 2
    return lvl, lives, mlives


def kimove(pl_pos, move, lvl, lives, mlives):
    print(pl_pos)
    print(move)
    print(lvl)
    print(lvl[0])
    lvl[pl_pos[0] + pl_pos[1]] = 3 # Fehler: pl_pos ist nicht für dieses lvl format! d.h. das ich mal wieder etwas
    # umschreiben muss -_-
    lvl[(move[0] + move[1])] = 2
    pl_pos = move
    return pl_pos, lvl, lives, mlives
