import sys
import os
import time
from src import mnlp, ca, gtps, dspl


class MBKI:
    def __init__(self, lvl, lives):
        self.lives = lives
        self.mlives = 4
        self.lvl_ut = [lvl]
        self.lvl = mnlp.init(lvl)
        self.fpos, self.ppos = self.get_positions()
        self.make_route()

    def get_positions(self):
        for y in range(len(self.lvl_ut[0])):
            for x in range(len(self.lvl_ut[0][y])):
                if self.lvl_ut[0][y][x] == "P":
                    self.ppos = (y, x)
                if self.lvl_ut[0][y][x] == "F":
                    self.fpos = (y, x)
        return self.fpos, self.ppos

    def dt(self, lvl_ut_new = [[], [], []], t=0):
        try:
            for i in self.lvl:
                if i == 1:
                    lvl_ut_new[t].append("X")
                elif i == 2:
                    lvl_ut_new[t].append("P")
                elif i == 3:
                    lvl_ut_new[t].append(" ")
                elif i == 4:
                    t+=1
                elif i == 5:
                    lvl_ut_new[t].append("G")
        except IndexError:
            pass
        return lvl_ut_new

    def make_route(self):
        while True:
            if self.ppos[1] > self.fpos[1]+1:
                self.use_route("l")
                self.lvl_ut = self.dt()
                self.fpos, self.ppos = self.get_positions()
            elif self.ppos[1]-1 < self.fpos[1]:
                self.use_route("r")
                self.lvl_ut = self.dt()
                self.fpos, self.ppos = self.get_positions()
            if self.ppos[1] == self.fpos[0]:
                break
            if self.ppos[0] > self.fpos[0]-1:
                self.use_route("u")
                self.lvl_ut = self.dt()
                self.fpos, self.ppos = self.get_positions()
            elif self.ppos[0] < self.fpos[0]+1:
                self.use_route("d")
                self.lvl_ut = self.dt()
                self.fpos, self.ppos = self.get_positions()
            if self.ppos[0] == self.fpos[1] and self.ppos[1] == self.fpos[0]:
                break

        while True:
            if self.ppos[1] > self.fpos[1]+1:
                self.use_route("l")
                self.lvl_ut = self.dt()
                self.fpos, self.ppos = self.get_positions()
            elif self.ppos[1]-1 < self.fpos[1]:
                self.use_route("r")
                self.lvl_ut = self.dt()
                self.fpos, self.ppos = self.get_positions()
            if self.ppos[1] == self.fpos[0]:
                break
            if self.ppos[0] > self.fpos[0]-1:
                self.use_route("u")
                self.lvl_ut = self.dt()
                self.fpos, self.ppos = self.get_positions()
            elif self.ppos[0] < self.fpos[0]+1:
                self.use_route("d")
                self.lvl_ut = self.dt()
                self.fpos, self.ppos = self.get_positions()
            if self.ppos[0] == self.fpos[1] and self.ppos[1] == self.fpos[0]:
                break

    def use_route(self, r):
        # This code is by Tornax07 thanks to him
        # For Windows
        if sys.platform == "win32":
            os.system('cls')
        # For Linux
        else:
            os.system('clear')

        if self.lives == 0:
            print("Game Over")
            exit()

        dspl.display_lvl(self.lvl, self.lives)
        self. lvl, self.lives, self.mlives = ca.move(gtps.get_player_pos(self.lvl), r, self.lvl, self.lives, self.mlives)
        time.sleep(0.5)
