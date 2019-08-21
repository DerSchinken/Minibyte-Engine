import turtle


class GameEngine:
    def __init__(self, lvl="", lvl_transformed=[]):
        wn = turtle.Screen()
        wn.bgcolor("black")
        wn.title("Game Engine")
        wn.setup(700, 700)

        pen = turtle.Turtle()
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.speed(0)

        player = turtle.Turtle()
        player.shape("circle")
        player.color("white")
        player.penup()
        player.speed(0)
        self.wn = wn
        self.pen = pen
        self.player = player
        GameEngine.edit_lvl(self)

    def play(self):
        while True:
            self.wn.update()

    def edit_lvl(self):
        return


GameEngine()
