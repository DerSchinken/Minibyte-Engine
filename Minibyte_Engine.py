"""""""""""""""""""""
    Game Engine
    By Dr.Bumm
    
    I Think i
   can call it
  a Game Engine
     but i'm
    not sure!
"""""""""""""""""""""
import os, time
import pygame
import sys
import termios
import tty
from threading import Thread

inkey_buffer = 1

def inkey():
    fd=sys.stdin.fileno()
    remember_attributes=termios.tcgetattr(fd)
    tty.setraw(sys.stdin.fileno())
    character=sys.stdin.read(inkey_buffer)
    termios.tcsetattr(fd,termios.TCSADRAIN, remember_attributes)
    return character

os.system('clear')

class Engine():
    def start(lvl):
        Engine.mainloop(lvl)
    
    def display_lvl(lvl, print_lvl=''):
        for i in range(len(lvl)):
            print_lvl += '\n'
            for x in lvl[i]:
                if x == 'X':
                    print_lvl += 'X'
                elif x == 'P':
                    print_lvl += '+'
                elif x == 'F':
                    print_lvl += ':'
                else:
                    print_lvl += ' '
                        
        return print_lvl

    def get_player_pos(lvl):
        for i in range(len(lvl)):
            player_pos = 0
            for x in lvl[i]:
                if x == 'P':  
                    return [i+1, player_pos+1]
                else:
                    player_pos += 1

    def move_player(lvl, player_pos):
        def mvpy(lvl, direction, player_pos):
            if direction == 'l':
                if lvl[player_pos[0]][player_pos[1]+1] == 'X':
                    pass
                elif lvl[player_pos[0]][player_pos[1]+1] == ':':
                    print('Level beendet')
                    time.sleep(3)
                    extit()
                elif lvl[player_pos[0]][player_pos[1]+1] == ' ':
                    lvl[player_pos[0]][player_pos[1]] = ' '
                    lvl[player_pos[0]][player_pos[1]+1] = 'P'
            elif direction == 'r':
                if lvl[player_pos[0]][player_pos[1]-1] == 'X':
                    pass
                elif lvl[player_pos[0]][player_pos[1]-1] == ':':
                    print('Level beendet')
                    time.sleep(3)
                    exit()
                elif lvl[player_pos[0]][player_pos[1]] == ' ':
                    lvl[player_pos[0]][player_pos[1]] = ' '
                    lvl[player_pos[0]][player_pos[1]-1] = 'P'
        
        key = Thread.start(inkey())
        print(key)
        if key in 'aA':
            mvpy(lvl, 'r', player_pos)
            
    def mainloop(lvl, delay=0.1):

        while True:
            try:
                time.sleep(delay)
                os.system('clear') # This is why the script must be run in a console
                print('FPS: {}'.format(delay * 100))
                Engine.move_player(lvl, Engine.get_player_pos(lvl))
                print(Engine.display_lvl(lvl))
            except KeyboardInterrupt:
                print('\nExiting Game')
                time.sleep(1)
                return

if __name__ == '__main__':
    print('warning: please be sure to start this script in a console')
    time.sleep(1)
    """
     Change the lvl to your own lvl
     Ps. only X's, space's, 1 P and 1 F are allowed!
     P = Player
     F = Finish
     X = wall
     Space = place who the player can move
    
     The P is an +
     The F is an :
     The X is an X
     The space is an space
    """
    lvl = [
        'XXXXXXXXXXX',
        'XF        X',
        'XXXXX XXXXX',
        'X        PX',
        'XXXXXXXXXXX'
        ]
    
    print('Press T to start the Game')
    while True:
        key = inkey()
        print(key)
        if key == 't':
            Engine.start(lvl)
            break
else:
    print('Hello from Dr.Bumm. Maybe you will \nvisit our website Index12.bplaced.net/programms\n\n')
    print('Warning: please be sure to start this script in a console')
    time.sleep(1)

