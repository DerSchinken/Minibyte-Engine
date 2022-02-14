import tkinter as tk  # Tkinter
import save_load_map  # Save and Load system

# width and height of the window
width = 800
height = 700


def ignore(*args, **kwargs):
    # ignore args
    for stuff in zip(kwargs, args):
        return stuff


def clamp(_min, _max, value) -> int or float:
    # clamp value between min and max
    return max(_min, min(_max, value))


class Window:
    def __init__(self, *, load_map=False, map_name=""):
        # Sets vars for the program
        self.map_name = map_name
        self.load_map = load_map
        self.lives = 6
        self.object_in_hand = "wall"
        self.buttons = []
        self.obj_buttons = []
        self.player_position = 0
        self.done = False
        self.root = tk.Tk()
        self.root.maxsize(width, height)
        self.root.minsize(width, height)
        self.root.attributes("-alpha", 0.87)
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        self.root.bind('<Control-s>', self.save)
        self.player_on_board = False
        self.canvas = tk.Canvas(self.root, height=height, width=width)
        self.canvas.pack()
        self.win_label = ""
        self.win_label2 = ""
        self.finish_on_board = 0

        # Load sprites
        self.wall_sprite = tk.PhotoImage(file="sprites/wall.png").subsample(x=50, y=50)
        self.floor_sprite = tk.PhotoImage(file="sprites/floor.png").subsample(x=6, y=6)
        self.player_sprite = tk.PhotoImage(file="sprites/player.png").subsample(x=15, y=20)
        self.finish_sprite = tk.PhotoImage(file="sprites/finish.png").subsample(x=15, y=15)
        self.enemy_sprite = tk.PhotoImage(file="sprites/enemy.png").subsample(x=6, y=6)

        # Configures frames
        self.frame1 = tk.Frame(self.root, bg="white")
        self.frame1.place(relwidth=1, relheight=0.25)
        self.frame1.pack(side="bottom")

        self.frame2 = tk.Frame(self.root, bg="white")
        self.frame2.place(relwidth=1, relheight=0.75)

        self.frame3 = tk.Frame(self.root, bg="white")
        self.frame3.place(relwidth=1, relheight=1)

        # Set the title
        self.root.title("Minibyte-Engine")

        # This is the button that is behind the label and starts the game if you click anywhere on the window
        self.button1 = tk.Button(self.frame3, text="", command=self.start)
        self.button1.place(relwidth=1, relheight=1)

        # Title screen
        self.text_label = tk.Label(self.frame3, text="Welcome to the Minibyte-Engine!!")
        self.text_label.place(relx=0.02, rely=0.45)
        self.text_label.config(font=("Courier", 30))

    def create_buttons(self):
        self.frame2.destroy()
        self.frame2 = tk.Frame(self.root, bg="white")
        self.frame2.place(relwidth=1, relheight=0.75)

        for i in range(0, 400):
            self.buttons.append(
                tk.Button(
                    self.frame2, text=str(i), bg='white', relief=tk.RIDGE, command=lambda _x=i: self.place_obj(_x)
                )
            )

        # Creates the buttons properties
        x, y = 0, 0
        for i in range(400):
            self.buttons[i].place(relx=0 + x, rely=0 + y, relwidth=0.05, relheight=0.05)
            self.buttons[i].config(fg="white", image=self.floor_sprite)
            x += 0.05
            if x >= 1.0:
                y += 0.05
                x = 0

    def start(self):
        self.frame3.destroy()  # Destroys the Title screen
        self.frame1.config(bg="white")
        self.frame2.config(bg="white")
        self.root.attributes("-alpha", 1)
        # print(len(self.buttons))
        if len(self.buttons) < 400:
            self.buttons = []
            self.create_buttons()  # Creates all the 400 buttons
        elif len(self.buttons) > 400:  # too many buttons
            raise Exception("Too many buttons")

        # Load Map
        if self.load_map:
            save_load_map.load(self.buttons, self.map_name, self)
            self.load_map = False  # This was the f*cking bug that I tried to fix for hours god-damn it

        # Create element choose bar
        self.obj_buttons.append(
            tk.Button(
                self.frame1, text="Wall", command=lambda: self.change_object_in_hand("wall"), relief=tk.FLAT
            )
        )
        self.obj_buttons[0].config(bg="black", fg="white")
        self.obj_buttons[0].pack(side=tk.LEFT)

        self.obj_buttons.append(
            tk.Button(
                self.frame1, text="Player", command=lambda: self.change_object_in_hand("player"), relief=tk.FLAT
            )
        )
        self.obj_buttons[1].config(bg="white", fg="black")
        self.obj_buttons[1].pack(side=tk.LEFT)  # , padx=40)

        self.obj_buttons.append(
            tk.Button(
                self.frame1, text="Gegner", command=lambda: self.change_object_in_hand("enemy"), relief=tk.FLAT
            )
        )
        self.obj_buttons[2].config(bg="white", fg="black")
        self.obj_buttons[2].pack(side=tk.LEFT)  # , padx=40)

        self.obj_buttons.append(
            tk.Button(
                self.frame1, text="Ziel", command=lambda: self.change_object_in_hand("finish"), relief=tk.FLAT
            )
        )
        self.obj_buttons[3].config(bg="white", fg="black")
        self.obj_buttons[3].pack(side=tk.LEFT)  # , padx=40)

        self.obj_buttons.append(
            tk.Button(
                self.frame1, text="Delete", command=lambda: self.change_object_in_hand("delete"), relief=tk.FLAT
            )
        )
        self.obj_buttons[4].config(bg="white", fg="black")
        self.obj_buttons[4].pack(side=tk.LEFT)  # , padx=40)

        self.obj_buttons.append(
            tk.Button(
                self.frame1, text="Save", command=self.save, relief=tk.FLAT
            )
        )
        self.obj_buttons[5].config(bg="white", fg="black")
        self.obj_buttons[5].pack(side=tk.LEFT)  # , padx=40)

        self.obj_buttons.append(
            tk.Button(
                self.frame1, text="Load", command=lambda: save_load_map.load_map(self), relief=tk.FLAT
            )
        )
        self.obj_buttons[6].config(bg="white", fg="black")
        self.obj_buttons[6].pack(side=tk.LEFT)  # , padx=40)

        self.obj_buttons.append(
            tk.Button(
                self.frame1, text="Play", command=self.play, relief=tk.FLAT
            )
        )
        self.obj_buttons[7].config(bg="white", fg="black")
        self.obj_buttons[7].pack(side=tk.LEFT)

        self.root.maxsize(width, height + 50)

    def place_obj(self, button_id):
        if self.object_in_hand == "wall":
            if self.buttons[int(button_id)]["text"] == "+":  # Checks if the object place is the player
                self.player_on_board = False  # If yes then set player_on_field to False
            self.buttons[int(button_id)].config(bg="black", text=" ", fg="black", image=self.wall_sprite)
            # And then set the place to the object
        elif self.object_in_hand == "player":  # The same as the first
            if not self.player_on_board:  # Checks if the player isn't on the field
                self.player_on_board = True  # When yes then set the player_on_field var. to True
                self.buttons[int(button_id)].config(bg="white", text="+", fg="black", font=("Courier", 20, "bold"),
                                                    image=self.player_sprite)  # And
                # then set the place to the player
        elif self.object_in_hand == "enemy":  # The same as the first
            if self.buttons[int(button_id)]["text"] == "+":
                self.player_on_board = False
            self.buttons[int(button_id)].config(bg="white", text="M", fg="black", font=("Courier", 30, "bold"),
                                                image=self.enemy_sprite)
        elif self.object_in_hand == "finish":  # The same as the first
            if self.buttons[int(button_id)]["text"] == "+":
                self.player_on_board = False
            self.buttons[int(button_id)].config(bg="white", text=":", fg="black", font=("Courier", 30, "bold"),
                                                image=self.finish_sprite)
            self.finish_on_board += 1
            self.buttons[int(button_id)]["text"] = ":"
        elif self.object_in_hand == "delete":  # The same as the first
            if self.buttons[int(button_id)]["text"] == "+":
                self.player_on_board = False
            elif self.buttons[int(button_id)]["text"] == ":":
                self.finish_on_board -= 1
            self.buttons[int(button_id)].config(bg="white", text="", fg="white", image=self.floor_sprite)

    def change_object_in_hand(self, change_to_object):
        self.object_in_hand = change_to_object

    def save(self, event=None):
        ignore(event)
        save_load_map.save_map(self)

    def play(self):
        if not self.finish_on_board > 0:
            return
        if not self.player_on_board:
            return
        save_load_map.save(self.buttons, "last_map", "temp_save_system")
        self.frame1.destroy()  # Destroys the element "choose bar"
        # self.frame1.place(relwidth=0, relheight=0)
        self.frame2.place(relwidth=1, relheight=1)  # Sets the playing area to (the) full  window/fullscreen
        self.object_in_hand = None  # Sets the element in your hand to none

        # Movement
        self.root.bind('<w>', lambda x: up())
        self.root.bind('<s>', lambda x: down())
        self.root.bind('<a>', lambda x: right())
        self.root.bind('<d>', lambda x: left())

        self.root.bind('<W>', lambda x: up())
        self.root.bind('<S>', lambda x: down())
        self.root.bind('<A>', lambda x: right())
        self.root.bind('<D>', lambda x: left())

        self.root.bind('<Up>', lambda x: up())
        self.root.bind('<Down>', lambda x: down())
        self.root.bind('<Left>', lambda x: right())
        self.root.bind('<Right>', lambda x: left())

        self.root.bind('<8>', lambda x: up())
        self.root.bind('<2>', lambda x: down())
        self.root.bind('<4>', lambda x: right())
        self.root.bind('<6>', lambda x: left())

        def up():
            # Get the player position
            for i in range(400):
                if self.buttons[i]["text"] == "+":
                    self.player_position = i
                    break
            try:
                # Try to change the position of th player
                if self.buttons[self.player_position - 20]["text"] != " " and \
                        self.buttons[self.player_position - 20]["text"] != "M" and \
                        self.buttons[self.player_position - 20]["text"] != ":":
                    self.buttons[self.player_position].config(text="", image=self.floor_sprite)
                    self.buttons[self.player_position - 20].config(text="+", fg="black", font=("Courier", 20, "bold"),
                                                                   image=self.player_sprite)
                if self.buttons[self.player_position - 20]["text"] == ":":
                    self.win()
                    self.unbid_move_keys()
                elif self.buttons[self.player_position - 20]["text"] == "M":
                    self.lives -= 1
                    if self.lives <= 0:
                        self.unbid_move_keys()
                        game_over = tk.Label(self.frame2, text="Game Over!\nYOU DIED!", font=("Courier", 30, "bold"))
                        game_over2 = tk.Label(self.frame2, text="Press space to continue", font=("Courier", 11, ""))
                        game_over.pack()
                        game_over2.pack()
                        self.root.bind("<space>", lambda x: self.continue_())
            except IndexError:
                self.buttons[self.player_position].config(text="+")

        def down():
            # Get the player position
            for i in range(400):
                if self.buttons[i]["text"] == "+":
                    self.player_position = i
                    break
            try:
                # Try to change the player position
                if self.buttons[self.player_position + 20]["text"] != " " and \
                        self.buttons[self.player_position + 20]["text"] != "M" and \
                        self.buttons[self.player_position + 20]["text"] != ":":
                    self.buttons[self.player_position].config(text="", image=self.floor_sprite)
                    self.buttons[self.player_position + 20].config(text="+", fg="black", font=("Courier", 20, "bold"),
                                                                   image=self.player_sprite)
                if self.buttons[self.player_position + 20]["text"] == ":":
                    self.win()
                    self.unbid_move_keys()
                elif self.buttons[self.player_position + 20]["text"] == "M":
                    self.lives -= 1
                    if self.lives <= 0:
                        self.unbid_move_keys()
                        game_over = tk.Label(self.frame2, text="Game Over!\nYOU DIED!", font=("Courier", 30, "bold"))
                        game_over2 = tk.Label(self.frame2, text="Press space to continue", font=("Courier", 11, ""))
                        game_over.pack()
                        game_over2.pack()
                        self.root.bind("<space>", lambda x: self.continue_())
            except IndexError:
                self.buttons[self.player_position].config(text="+")

        def right():
            # Get the player position
            for i in range(400):
                if self.buttons[i]["text"] == "+":
                    self.player_position = i
                    break
            try:
                # Try to change the player position
                if self.buttons[self.player_position - 1]["text"] != " " and \
                        self.buttons[self.player_position - 1]["text"] != "M" and \
                        self.buttons[self.player_position - 1]["text"] != ":":
                    self.buttons[self.player_position].config(text="", image=self.floor_sprite)
                    self.buttons[self.player_position - 1].config(text="+", fg="black", font=("Courier", 20, "bold"),
                                                                  image=self.player_sprite)
                if self.buttons[self.player_position - 1]["text"] == ":":
                    self.win()
                    self.unbid_move_keys()
                elif self.buttons[self.player_position - 1]["text"] == "M":
                    self.lives -= 1
                    if self.lives <= 0:
                        self.unbid_move_keys()
                        game_over = tk.Label(self.frame2, text="Game Over!\nYOU DIED!", font=("Courier", 30, "bold"))
                        game_over2 = tk.Label(self.frame2, text="Press space to continue", font=("Courier", 11, ""))
                        game_over.pack()
                        game_over2.pack()
                        self.root.bind("<space>", lambda x: self.continue_())
            except IndexError:
                self.buttons[self.player_position].config(text="+")

        def left():
            # Get the player position
            for i in range(400):
                if self.buttons[i]["text"] == "+":
                    self.player_position = i
                    break
            try:
                # Try to change the player position
                if self.buttons[self.player_position + 1]["text"] != " " and \
                        self.buttons[self.player_position + 1]["text"] != "M" and \
                        self.buttons[self.player_position + 1]["text"] != ":":
                    self.buttons[self.player_position].config(text="", image=self.floor_sprite)
                    self.buttons[self.player_position + 1].config(text="+", fg="black", font=("Courier", 20, "bold"),
                                                                  image=self.player_sprite)
                if self.buttons[self.player_position + 1]["text"] == ":":
                    self.win()
                    self.unbid_move_keys()
                elif self.buttons[self.player_position + 1]["text"] == "M":
                    self.lives -= 1
                    if self.lives <= 0:
                        self.unbid_move_keys()
                        game_over = tk.Label(self.frame2, text="Game Over!\nYOU DIED!", font=("Courier", 30, "bold"))
                        game_over2 = tk.Label(self.frame2, text="Press space to continue", font=("Courier", 11, ""))
                        game_over.pack()
                        game_over2.pack()
                        self.root.bind("<space>", lambda x: self.continue_())
            except IndexError:
                self.buttons[self.player_position].config(text="+")

    def win(self):
        self.frame1.destroy()
        self.win_label = tk.Label(self.frame2, text="You Win!", font=("Courier", 30, "bold"))
        self.win_label2 = tk.Label(self.frame2, text="Press space to continue", font=("Courier", 11, ""))
        self.win_label.pack()
        self.win_label2.pack()

        self.root.bind("<space>", lambda x: self.continue_())

    def continue_(self):
        self.frame2.destroy()
        self.frame1 = tk.Frame()
        self.frame2 = tk.Frame()
        self.root.unbind("<space>")
        # self.win_label.destroy()
        # self.win_label2.destroy()
        self.buttons = []
        self.obj_buttons = []
        self.frame1.place(relwidth=1, relheight=0.25)
        self.frame2.place(relwidth=1, relheight=0.75)
        self.frame1.pack(side=tk.BOTTOM)
        self.create_buttons()
        self.buttons = save_load_map.load(self.buttons, "last_map by temp_save_system", self)
        self.start()

    def unbid_move_keys(self):
        # Unbind all the movement keys to avoid errors
        self.root.unbind("<w>")
        self.root.unbind("<a>")
        self.root.unbind("<s>")
        self.root.unbind("<d>")

        self.root.unbind("<W>")
        self.root.unbind("<A>")
        self.root.unbind("<S>")
        self.root.unbind("<D>")

        self.root.unbind("<8>")
        self.root.unbind("<4>")
        self.root.unbind("<6>")
        self.root.unbind("<2>")

        self.root.unbind("<Up>")
        self.root.unbind("<Down>")
        self.root.unbind("<Left>")
        self.root.unbind("<Right>")

    def mainloop(self):
        # mainloop
        self.root.mainloop()


# For testing:
if __name__ == "__main__":
    window = Window(load_map=True, map_name="Test MAP by DerSchinken (Dr.Bumm)")
    window.mainloop()
