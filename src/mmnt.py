# Movement

import time
from src import ca, gtps


def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch

    # POSIX system. Create and return a getch that manipulates the tty.
    import sys
    import tty

    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch


def mv(lvl, lives, mlives,  done=False):
    getch = _find_getch()
    while not done:
        key = getch()
        # print(key)
        if key != '':
            if key == b'a':
                done = True
                return ca.move(gtps.get_player_pos(lvl), 'l', lvl, lives, mlives)
            if key == b'd':
                done = True
                return ca.move(gtps.get_player_pos(lvl), 'r', lvl, lives, mlives)
            if key == b'w':
                done = True
                return ca.move(gtps.get_player_pos(lvl), 'u', lvl, lives, mlives)
            if key == b's':
                done = True
                return ca.move(gtps.get_player_pos(lvl), 'd', lvl, lives, mlives)
            if key == b'\x03':
                print('Exiting')
                time.sleep(3)
                exit()
                
        if key != '':
            if key == 'a':
                done = True
                return ca.move(gtps.get_player_pos(lvl), 'l', lvl, lives, mlives)
            if key == 'd':
                done = True
                return ca.move(gtps.get_player_pos(lvl), 'r', lvl, lives, mlives)
            if key == 'w':
                done = True
                return ca.move(gtps.get_player_pos(lvl), 'u', lvl, lives, mlives)
            if key == 's':
                done = True
                return ca.move(gtps.get_player_pos(lvl), 'd', lvl, lives, mlives)
            if key == '':
                print('Exiting')
                time.sleep(3)
                exit()
