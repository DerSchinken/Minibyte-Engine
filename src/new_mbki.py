from src import mnlp, dspl, ca
import time
import sys
import os


class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:

        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            if maze[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(current_node, node_position)

            children.append(new_node)

        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)


def getsaep(lvl, fpos=(), ppos=()):
    #print(lvl)
    for y in range(len(lvl)):
        for x in range(len(lvl[y])):
            if lvl[y][x] == "P":
                ppos = (y, x)
            if lvl[y][x] == "F":
                fpos = (x, y)
    return fpos, ppos


def main(lvl, lives, mlives):

    maze = mnlp.getmaze(lvl)

    end, start = getsaep(lvl)

    path = astar(maze, start, end)

    lvl_dspl = dspl.init(lvl)

    print(maze)
    print(end, start)
    print(lvl)
    print(maze)
    #for i in range(len(path)-1):
    #   print(str(path[i][i] + path[i+1][i+1]))
    #exit()
    #print(lvl_dspl)
    #print(lvl)

    for move in path:
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
        #print(path)
        dspl.display_lvl(lvl_dspl, lives)
        start, lvl_dspl, lives, mlives = ca.kimove(list(start), list(move), lvl_dspl, lives, mlives)
        time.sleep(0.5)
        print(lvl_dspl)

