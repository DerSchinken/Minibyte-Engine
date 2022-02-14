import os
from tkinter import *
from shutil import *


def compiler(self):
    def save_info(map, author, map_name, self):
        game_name = map.get()
        author = author.get()
        map_name = map_name.get()
        compile_(game_name, author, map_name)
        screen.destroy()

    screen = Tk()
    screen.geometry("500x500")
    screen.title("Compiler")
    heading = Label(screen, text="Compile", bg="grey", fg="black", width="500", height="3")
    heading.pack()

    map_text = Label(screen, text="Game Name ", )
    author_text = Label(screen, text="Author Name  ", )
    map_name = Label(screen, text="Map Name  ", )
    map_text.place(x=15, y=70)
    author_text.place(x=15, y=140)
    map_name.place(x=15, y=210)

    game_name = StringVar()
    author = StringVar()
    map = StringVar()

    game_name_entry = Entry(screen, textvariable=game_name, width="30")
    author_entry = Entry(screen, textvariable=author, width="30")
    map_entry = Entry(screen, textvariable=map, width="30")

    game_name_entry.place(x=15, y=100)
    author_entry.place(x=15, y=180)
    map_entry.place(x=15, y=260)

    save_button = Button(screen, text="Compile", width="30", height="2", command=lambda: save_info(game_name_entry, author_entry, map_entry, self), bg="grey")
    save_button.place(x=15, y=350)


def compile_(game_name, author, map_name):
    copytree("fbsrc\\", f"builds\\{game_name}\\")
    data = open(f"builds\\{game_name}\\data.MBD", "r").read().split("\n")
    data[1] += f"{map_name}"
    data[2] += f"{game_name}"
    data[3] += f"{author}"

    f = open(f"builds\\{game_name}\\data.MBD", "w")
    for i in range(len(data)):
        f.write(data[i] + "\n")
    f.close()

    copytree(f"Maps\\", f"builds\\{game_name}\\Maps\\")
