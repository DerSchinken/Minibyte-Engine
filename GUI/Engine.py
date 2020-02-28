import tkinter as tk  # Tkinter
import buttons  # Those are the hardcoded 400 buttons
import save_load_map  # Save and Load system

# width and height of the window
width = 800
height = 700


class Window:
    def __init__(self, load_map=False, map_name=""):
        # Sets vars for the programm
        self.blst = []
        self.map_name = map_name
        self.load_map = load_map
        self.lives = 6
        self.objih = "wall"
        self.o = 0.0
        self.x = 0.0
        self.y = 0.0
        self.i = 0
        self.buttons = []
        self.obj_buttons = []
        self.ppos = 0
        self.done = False
        self.root = tk.Tk()
        self.root.maxsize(width, height)
        self.root.minsize(width, height)
        self.root.attributes("-alpha", 0.87)
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        self.root.bind('<Control-s>', self.save)
        self.player_on_field = False
        self.canvas = tk.Canvas(self.root, height=height, width=width)
        self.canvas.pack()
        self.win_label = ""
        self.win_label2 = ""

        # Load sprites
        self.wall_sprite = tk.PhotoImage(file="sprites\\wall.png").subsample(x=50, y=50)
        self.floor_sprite = tk.PhotoImage(file="sprites\\floor.png").subsample(x=6, y=6)
        self.player_sprite = tk.PhotoImage(file="sprites\\player.png").subsample(x=15, y=20)
        self.finisch_sprite = tk.PhotoImage(file="sprites\\finisch.png").subsample(x=15, y=15)
        self.enemie_sprite = tk.PhotoImage(file="sprites\\enemie.png").subsample(x=6, y=6)

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

    def start(self):
        self.frame3.destroy()  # Destroys the Title screen
        self.frame1.config(bg="white")
        self.frame2.config(bg="white")
        self.root.attributes("-alpha", 1)
        buttons.create_buttons(self, tk)  # Creates all the 400 buttons (Hardcoded)

        # Creates the buttons properties
        for i in range(400):
            self.buttons[i].place(relx=0+self.x, rely=0+self.y, relwidth=0.05, relheight=0.05)
            self.buttons[i].config(fg="white", image=self.floor_sprite)
            self.x += 0.05
            if self.x >= 1.0:
                self.y += 0.05
                self.x = 0

        # Load Map
        if self.load_map:
            save_load_map.load_map(self.buttons, self.map_name, self)

        # Create element choose bar
        self.obj_buttons.append(tk.Button(self.frame1, text="Wall", command=lambda : self.change_objih("wall"),
                                          relief=tk.FLAT))
        self.obj_buttons[0].config(bg="black", fg="white")
        self.obj_buttons[0].pack(side=tk.LEFT)

        self.obj_buttons.append(tk.Button(self.frame1, text="Player", command=lambda : self.change_objih("player"),
                                          relief=tk.FLAT))
        self.obj_buttons[1].config(bg="white", fg="black")
        self.obj_buttons[1].pack(side=tk.LEFT, padx=50)

        self.obj_buttons.append(tk.Button(self.frame1, text="Gegner", command=lambda : self.change_objih("enemie"),
                                          relief=tk.FLAT))
        self.obj_buttons[2].config(bg="white", fg="black")
        self.obj_buttons[2].pack(side=tk.LEFT, padx=50)

        self.obj_buttons.append(tk.Button(self.frame1, text="Ziel", command=lambda: self.change_objih("finish"),
                                          relief=tk.FLAT))
        self.obj_buttons[3].config(bg="white", fg="black")
        self.obj_buttons[3].pack(side=tk.LEFT, padx=50)

        self.obj_buttons.append(tk.Button(self.frame1, text="Delete", command=lambda: self.change_objih("delete"),
                                          relief=tk.FLAT))
        self.obj_buttons[4].config(bg="white", fg="black")
        self.obj_buttons[4].pack(side=tk.LEFT, padx=50)

        self.obj_buttons.append(tk.Button(self.frame1, text="Save", command=self.save, relief=tk.FLAT))
        self.obj_buttons[5].config(bg="white", fg="black")
        self.obj_buttons[5].pack(side=tk.LEFT, padx=50)

        self.obj_buttons.append(tk.Button(self.frame1, text="Play", command=self.play, relief=tk.FLAT))
        self.obj_buttons[6].config(bg="white", fg="black")
        self.obj_buttons[6].pack(side=tk.LEFT)

        self.root.maxsize(width, height+50)

    def place_obj(self, btid):
        if self.objih == "wall":
            if self.buttons[int(btid)]["text"] == "+":  # Checks if the object place place is the player
                self.player_on_field = False  # If yes then set player_on_field to False
            self.buttons[int(btid)].config(bg="black", text=" ", fg="black", image=self.wall_sprite)  # And then set
            # the place to the object
        elif self.objih == "player":  # The same as the first
            if not self.player_on_field:  # Checks if the player is't on the field
                self.player_on_field = True  # When yes then set the player_on_field var. to True
                self.buttons[int(btid)].config(bg="white", text="+", fg="black", font=("Courier", 20, "bold"), image=self.player_sprite)  # And
                # then set the place to the player
        elif self.objih == "enemie":  # The same as the first
            if self.buttons[int(btid)]["text"] == "+":
                self.player_on_field = False
            self.buttons[int(btid)].config(bg="white", text="M", fg="black", font=("Courier", 30, "bold"), image=self.enemie_sprite)
        elif self.objih == "finish":  # The same as the first
            if self.buttons[int(btid)]["text"] == "+":
                self.player_on_field = False
            self.buttons[int(btid)].config(bg="white", text=":", fg="black", font=("Courier", 30, "bold"), image=self.finisch_sprite)
        elif self.objih == "delete":  # The same as the first
            if self.buttons[int(btid)]["text"] == "+":
                self.player_on_field = False
            self.buttons[int(btid)].config(bg="white", text="", fg="white", image=self.floor_sprite)

    def change_objih(self, ctobj):
        self.objih = ctobj

    def save(self, event=None):
        save_load_map.save_map(self)

    def play(self):
        save_load_map.save_map(self.buttons, "last_map", "temp_save_system")
        self.frame1.destroy()  # Destroys the element "choose bar"
        #self.frame1.place(relwidth=0, relheight=0)
        self.frame2.place(relwidth=1, relheight=1)  # Sets the playing area to (the) full  window/fullscreen
        self.objih = None  # Sets the element in your hand to none

        # Movement
        self.root.bind('<w>', lambda x: up(self))
        self.root.bind('<s>', lambda x: down(self))
        self.root.bind('<a>', lambda x: right(self))
        self.root.bind('<d>', lambda x: left(self))

        self.root.bind('<W>', lambda x: up(self))
        self.root.bind('<S>', lambda x: down(self))
        self.root.bind('<A>', lambda x: right(self))
        self.root.bind('<D>', lambda x: left(self))

        self.root.bind('<Up>', lambda x: up(self))
        self.root.bind('<Down>', lambda x: down(self))
        self.root.bind('<Left>', lambda x: right(self))
        self.root.bind('<Right>', lambda x: left(self))

        self.root.bind('<8>', lambda x: up(self))
        self.root.bind('<2>', lambda x: down(self))  # This doesn't bind
        self.root.bind('<4>', lambda x: right(self))  # This doesn't bind
        self.root.bind('<6>', lambda x: left(self))

        def up(self):
            # Get the player position
            for i in range(400):
                if self.buttons[i]["text"] == "+":
                    self.ppos = i
                    break
            try:
                # Try to change the position of th player
                if self.buttons[self.ppos-20]["text"] != " " and self.buttons[self.ppos-20]["text"] != "M" and \
                        self.buttons[self.ppos-20]["text"] != ":":
                    self.buttons[self.ppos].config(text="", image=self.floor_sprite)
                    self.buttons[self.ppos-20].config(text="+", fg="black", font=("Courier", 20, "bold"), image=self.player_sprite)
                if self.buttons[self.ppos-20]["text"] == ":":
                    self.win()
                    self.unbid_move_keys()
                elif self.buttons[self.ppos-20]["text"] == "M":
                    self.lives -= 1
                    if self.lives <= 0:
                        self.unbid_move_keys()
                        game_over = tk.Label(self.frame2, text="Game Over!\nYOU DIED!", font=("Courier", 30, "bold"))
                        game_over2 = tk.Label(self.frame2, text="Press space to continue", font=("Courier", 11, ""))
                        game_over.pack()
                        game_over2.pack()
                        self.root.bind("<space>", lambda x: self.continue_())
            except IndexError:
                self.buttons[self.ppos].config(text="+")

        def down(self):
            # Get the player position
            for i in range(400):
                if self.buttons[i]["text"] == "+":
                    self.ppos = i
                    break
            try:
                # Try to change the player position
                if self.buttons[self.ppos+20]["text"] != " " and self.buttons[self.ppos+20]["text"] != "M" and \
                        self.buttons[self.ppos+20]["text"] != ":":
                    self.buttons[self.ppos].config(text="", image=self.floor_sprite)
                    self.buttons[self.ppos+20].config(text="+", fg="black", font=("Courier", 20, "bold"), image=self.player_sprite)
                if self.buttons[self.ppos+20]["text"] == ":":
                    self.win()
                    self.unbid_move_keys()
                elif self.buttons[self.ppos+20]["text"] == "M":
                    self.lives -= 1
                    if self.lives <= 0:
                        self.unbid_move_keys()
                        game_over = tk.Label(self.frame2, text="Game Over!\nYOU DIED!", font=("Courier", 30, "bold"))
                        game_over2 = tk.Label(self.frame2, text="Press space to continue", font=("Courier", 11, ""))
                        game_over.pack()
                        game_over2.pack()
                        self.root.bind("<space>", lambda x: self.continue_())
            except IndexError:
                self.buttons[self.ppos].config(text="+")

        def right(self):
            # Get the player position
            for i in range(400):
                if self.buttons[i]["text"] == "+":
                    self.ppos = i
                    break
            try:
                # Try to change the player position
                if self.buttons[self.ppos-1]["text"] != " " and self.buttons[self.ppos-1]["text"] != "M" and \
                        self.buttons[self.ppos-1]["text"] != ":":
                    self.buttons[self.ppos].config(text="", image=self.floor_sprite)
                    self.buttons[self.ppos-1].config(text="+", fg="black", font=("Courier", 20, "bold"), image=self.player_sprite)
                if self.buttons[self.ppos-1]["text"] == ":":
                    self.win()
                    self.unbid_move_keys()
                elif self.buttons[self.ppos-1]["text"] == "M":
                    self.lives -= 1
                    if self.lives <= 0:
                        self.unbid_move_keys()
                        game_over = tk.Label(self.frame2, text="Game Over!\nYOU DIED!", font=("Courier", 30, "bold"))
                        game_over2 = tk.Label(self.frame2, text="Press space to continue", font=("Courier", 11, ""))
                        game_over.pack()
                        game_over2.pack()
                        self.root.bind("<space>", lambda x: self.continue_())
            except IndexError:
                self.buttons[self.ppos].config(text="+")

        def left(self):
            # Get the player position
            for i in range(400):
                if self.buttons[i]["text"] == "+":
                    self.ppos = i
                    break
            try:
                # Try to change the player position
                if self.buttons[self.ppos+1]["text"] != " " and self.buttons[self.ppos+1]["text"] != "M" and \
                        self.buttons[self.ppos+1]["text"] != ":":
                    self.buttons[self.ppos].config(text="", image=self.floor_sprite)
                    self.buttons[self.ppos+1].config(text="+", fg="black", font=("Courier", 20, "bold"), image=self.player_sprite)
                if self.buttons[self.ppos+1]["text"] == ":":
                    self.win()
                    self.unbid_move_keys()
                elif self.buttons[self.ppos+1]["text"] == "M":
                    self.lives -= 1
                    if self.lives <= 0:
                        self.unbid_move_keys()
                        game_over = tk.Label(self.frame2, text="Game Over!\nYOU DIED!", font=("Courier", 30, "bold"))
                        game_over2 = tk.Label(self.frame2, text="Press space to continue", font=("Courier", 11, ""))
                        game_over.pack()
                        game_over2.pack()
                        self.root.bind("<space>", lambda x: self.continue_())
            except IndexError:
                self.buttons[self.ppos].config(text="+")

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
        #self.win_label.destroy()
        #self.win_label2.destroy()
        self.buttons = []
        self.x = 0
        self.y = 0
        self.obj_buttons = []
        self.frame1.place(relwidth=1, relheight=0.25)
        self.frame2.place(relwidth=1, relheight=0.75)
        self.frame1.pack(side=tk.BOTTOM)
        buttons.create_buttons(self, tk)  # Creates all the 400 buttons (Hardcoded)
        save_load_map.load_map(self.buttons, "last_map by temp_save_system", self)
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
    window = Window(load_map=True, map_name="Test MAP by Dr.Bumm")
    window.mainloop()
