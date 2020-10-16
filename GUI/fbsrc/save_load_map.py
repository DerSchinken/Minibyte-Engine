import os
#os.chdir("C:/users/paulh/Desktop/Minibyte-Engine-master/GUI/fbsrc/Maps")


def load(buttons, map_name, self):
    map_ = open("Maps/" + map_name, "r").read().split(";")  # reads the button properties
    for i in range(400):  # Changes the new buttons properties with the old (the saved version) properties
        if map_[i] != " ":
            if map_[i] == "+":
                self.ppos = i
                buttons[i].config(text="*", font=("Courier", 20, "bold"), fg="black", image=self.player_sprite)
            elif map_[i] == "M":
                buttons[i].config(text="M", font=("Courier", 30, "bold"), fg="black", image=self.enemy_sprite)
            elif map_[i] == ":":
                buttons[i].config(text=":", font=("Courier", 30, "bold"), fg="black", image=self.finish_sprite)
        else:
            buttons[i].config(bg="black", fg="black", text=" ", image=self.wall_sprite)
