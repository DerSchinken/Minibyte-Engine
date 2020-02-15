def save_map(map_, map_name, author="Nicht angegeben"):  # map_ because of the built-in function map
    for map_tile in map_:
        open("Maps\\" + map_name + " by " + author + ".MBE", "a").write(str(map_tile["text"]) + ";")  # Saves the button properties


def load_map(buttons, map_name, self):
    map_ = open("Maps\\" + map_name + ".MBE", "r").read().split(";")  # reads the button properties
    for i in range(400):  # Changes the new buttons properties with the old (the saved version) properties
        if map_[i] != " ":
            if map_[i] == "+":
                buttons[i].config(text=map_[i], font=("Courier", 20, "bold"), fg="black", image=self.player_sprite)
            elif map_[i] == "M":
                buttons[i].config(text=map_[i], font=("Courier", 30, "bold"), fg="black", image=self.enemie_sprite)
            elif map_[i] == ":":
                buttons[i].config(text=map_[i], font=("Courier", 30, "bold"), fg="black", image=self.finisch_sprite)
        else:
            buttons[i].config(bg="black", fg="black", text=map_[i], image=self.wall_sprite)
