from tkinter import *
from typing import List


def save_map(self):
    def save_info(map, author, self):
        map_name = map.get()
        author = author.get()
        save(self.buttons, map_name, author)
        screen.destroy()

    screen = Tk()
    screen.geometry("500x500")
    screen.title("Save Map")
    heading = Label(screen, text="Save Map", bg="grey", fg="black", width="500", height="3")
    heading.pack()

    map_text = Label(screen, text="Map Name ", )
    author_text = Label(screen, text="Author Name  ", )
    map_text.place(x=15, y=70)
    author_text.place(x=15, y=140)

    map = StringVar()
    author = StringVar()

    map_entry = Entry(screen, textvariable=map, width="30")
    author_entry = Entry(screen, textvariable=author, width="30")

    map_entry.place(x=15, y=100)
    author_entry.place(x=15, y=180)

    save_button = Button(screen, text="Save", width="30", height="2", command=lambda: save_info(map_entry, author_entry, self), bg="grey")
    save_button.place(x=15, y=290)


def load_map(self):
    # noinspection PyShadowingNames
    def load_info(_map, author, self):
        map_name = _map.get()
        author = author.get()
        self.buttons = load(self.buttons, str(map_name) + " by " + str(author), self)
        screen.destroy()

    screen = Tk()
    screen.geometry("500x500")
    screen.title("Load Map")
    heading = Label(screen, text="Load Map", bg="grey", fg="black", width="500", height="3")
    heading.pack()

    map_text = Label(screen, text="Map Name ", )
    author_text = Label(screen, text="Author Name  ", )
    map_text.place(x=15, y=70)
    author_text.place(x=15, y=140)

    _map = StringVar()
    author = StringVar()

    map_entry = Entry(screen, textvariable=_map, width=30)
    author_entry = Entry(screen, textvariable=author, width=30)

    map_entry.place(x=15, y=100)
    author_entry.place(x=15, y=180)

    save_button = Button(screen, text="Load", width="30", height="2", command=lambda: load_info(map_entry,
                                                                                                author_entry, self),
                         bg="grey")
    save_button.place(x=15, y=290)


def save(map_, map_name, author="Nicht angegeben"):  # map_ because of the built-in function map
    # print("ayooo")
    open("Maps/" + map_name + " by " + author + ".MBE", "w").write("")
    # print(len(open("Maps/" + map_name + " by " + author + ".MBE", "r").read()))

    for map_tile in map_:
        # Saves the button properties
        with open("Maps/" + map_name + " by " + author + ".MBE", "a") as _map:
            _map.write(str(map_tile["text"]) + ";")


def load(buttons: List[Button], map_name, self):
    map_ = open("Maps/" + map_name + ".MBE", "r").read().split(";")  # reads the button properties
    # self.create_buttons()
    
    for i in range(400):  # Changes the new buttons properties with the old (the saved version) properties
        if map_[i] != " ":
            if map_[i] == "+":
                buttons[i].config(text="+", font=("Courier", 20, "bold"), fg="black", image=self.player_sprite)
                self.player_on_board = True
            elif map_[i] == "M":
                buttons[i].config(text="M", font=("Courier", 30, "bold"), fg="black", image=self.enemy_sprite)
            elif map_[i] == ":":
                buttons[i].config(text=":", font=("Courier", 30, "bold"), fg="black", image=self.finish_sprite)
                self.finish_on_board = True
            else:
                buttons[i].config(text=map_[i], font=("Courier", 30, "bold"), fg="black", image=self.floor_sprite)
        else:
            buttons[i].config(bg="white", fg="black", text=" ", image=self.wall_sprite)

    return buttons
