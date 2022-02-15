from tkinter import *
from shutil import *
import os

data_template = """
[general_data]
map_name={}
title={}
author={}
width={}
height={}

[extra_modules]
{}
"""


def compiler():
    # noinspection PyShadowingNames
    def save_info(title, author, map_name, width, height):
        game_name = title.get()
        author = author.get()
        map_name = map_name.get()
        width = width.get()
        height = height.get()
        compile_(game_name, author, map_name, width, height)
        screen.destroy()

    screen = Tk()
    screen.geometry("500x500")
    screen.title("Compiler")
    heading = Label(screen, text="Compile", bg="grey", fg="black", width="500", height="3")
    heading.pack()

    title_text = Label(screen, text="Game Name ", )
    author_text = Label(screen, text="Author Name  ", )
    map_name_text = Label(screen, text="Map Name  ", )
    width_text = Label(screen, text="Width  ", )
    height_text = Label(screen, text="Height  ", )
    title_text.place(x=15, y=70)
    author_text.place(x=15, y=140)
    map_name_text.place(x=15, y=210)
    width_text.place(x=15, y=280)
    height_text.place(x=200, y=280)

    title = StringVar()
    author = StringVar()
    map_name = StringVar()
    width = StringVar()
    height = StringVar()

    game_name_entry = Entry(screen, textvariable=title, width=30)
    author_entry = Entry(screen, textvariable=author, width=30)
    map_entry = Entry(screen, textvariable=map_name, width=30)
    width_entry = Entry(screen, textvariable=width, width=30)
    height_entry = Entry(screen, textvariable=height, width=30)

    game_name_entry.place(x=15, y=100)
    author_entry.place(x=15, y=180)
    map_entry.place(x=15, y=260)
    width_entry.place(x=15, y=310)
    height_entry.place(x=200, y=310)

    save_button = Button(
        screen, text="Compile", width="30", height="2",
        command=lambda: save_info(game_name_entry, author_entry, map_entry, width_entry, height_entry),
        bg="grey"
    )
    save_button.place(x=15, y=350)

    screen.mainloop()


def compile_(game_name, author, map_name, width, height):
    copytree("fbsrc\\", f"builds\\{game_name}\\")
    data = open(f"builds\\{game_name}\\data.MBD", "r").read().split("\n")
    data[1] += f"{map_name}"
    data[2] += f"{game_name}"
    data[3] += f"{author}"
    data[4] += f"{width}"
    data[5] += f"{height}"

    f = open(f"builds\\{game_name}\\data.MBD", "w")
    for i in range(len(data)):
        f.write(data[i] + "\n")
    f.close()

    copytree(f"Maps\\", f"builds\\{game_name}\\Maps\\")
    os.rename(f"builds\\{game_name}\\Engine.exe", f"builds\\{game_name}\\{game_name}.exe")


if __name__ == "__main__":
    compiler()
