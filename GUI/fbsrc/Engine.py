import tkinter as tk  # Tkinter
import save_load_map  # Save and Load system

width = 800
height = 700


class Window:
    def __init__(self):
        # Sets vars for the program
        self.blst = []
        self.lives = 6
        self.o = 0.0
        self.x = 0.0
        self.y = 0.0
        self.buttons = []
        self.ppos = 0
        self.done = False
        self.root = tk.Tk()
        self.root.maxsize(width, height)
        self.root.minsize(width, height)
        self.root.attributes("-alpha", 0.87)
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        self.canvas = tk.Canvas(self.root, height=height, width=width)
        self.canvas.pack()
        self.win_label = ""
        self.win_label2 = ""
        self.map_name = open("data.MBD", "r").read().split("\n")[1].split("\"")[1]

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
        self.root.title(open("data.MBD", "r").read().split("\n")[1].split("\"")[1])

        # This is the button that is behind the label and starts the game if you click anywhere on the window
        self.button1 = tk.Button(self.frame3, text="", command=lambda x=1: self.play())
        self.button1.place(relwidth=1, relheight=1)

        # Title screen
        self.text_label = tk.Label(self.frame3, text="This was made with the\n Minibyte-Engine!")
        self.text_label.place(relx=0.17, rely=0.42)
        self.text_label.config(font=("Courier", 30))

    def create_buttons(self):
        for i in range(0, 400):
            self.buttons.append(
                tk.Button(self.frame2, text=str(i), bg='white', relief=tk.RIDGE, command=lambda x=1: print(None)))

    def play(self):
        self.root.attributes("-alpha", 1.0)
        self.frame3.destroy()
        self.frame2.place(relwidth=1, relheight=1)  # Sets the playing area to (the) full  window/fullscreen
        self.create_buttons()
        # Creates the buttons properties
        for i in range(400):
            self.buttons[i].place(relx=0 + self.x, rely=0 + self.y, relwidth=0.05, relheight=0.05)
            self.buttons[i].config(fg="white", image=self.floor_sprite)
            self.x += 0.05
            if self.x >= 1.0:
                self.y += 0.05
                self.x = 0
        save_load_map.load(self.buttons, self.map_name + ".MBE", self)

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
        self.root.bind('<2>', lambda x: down())  # This doesn't bind
        self.root.bind('<4>', lambda x: right())  # This doesn't bind
        self.root.bind('<6>', lambda x: left())

        def up():
            # Get the player position
            for o in range(400):
                if self.buttons[o]["text"] == "+":
                    self.ppos = o
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
                        game_over2 = tk.Label(self.frame2, text="Press space to exit", font=("Courier", 11, ""))
                        game_over.pack()
                        game_over2.pack()
                        self.root.bind("<space>", lambda x: self.root.destroy())
            except IndexError:
                self.buttons[self.ppos].config(text="+")

        def down():
            # Get the player position
            for p in range(400):
                if self.buttons[p]["text"] == "+":
                    self.ppos = p
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
                        game_over2 = tk.Label(self.frame2, text="Press space to exit", font=("Courier", 11, ""))
                        game_over.pack()
                        game_over2.pack()
                        self.root.bind("<space>", lambda x: self.root.destroy())
            except IndexError:
                self.buttons[self.ppos].config(text="+")

        def right():
            # Get the player position
            for z in range(400):
                if self.buttons[z]["text"] == "+":
                    self.ppos = z
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
                        game_over2 = tk.Label(self.frame2, text="Press space to exit", font=("Courier", 11, ""))
                        game_over.pack()
                        game_over2.pack()
                        self.root.bind("<space>", lambda x: self.root.destroy())
            except IndexError:
                self.buttons[self.ppos].config(text="+")

        def left():
            # Get the player position
            for u in range(400):
                if self.buttons[u]["text"] == "+":
                    self.ppos = u
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
                        game_over2 = tk.Label(self.frame2, text="Press space to exit", font=("Courier", 11, ""))
                        game_over.pack()
                        game_over2.pack()
                        self.root.bind("<space>", lambda x: self.root.destroy())
            except IndexError:
                self.buttons[self.ppos].config(text="+")

    def win(self):
        self.frame1.destroy()
        self.win_label = tk.Label(self.frame2, text="You Win!", font=("Courier", 30, "bold"))
        self.win_label2 = tk.Label(self.frame2, text="Press space to exit", font=("Courier", 11, ""))
        self.win_label.pack()
        self.win_label2.pack()

        self.root.bind("<space>", lambda x: self.root.destroy())

    def exit_app(self):
        self.root.destroy()

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


window = Window()
window.mainloop()
