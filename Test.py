from src.core import *
from src.addons import *

game_window = Window()
game_window.geometry("800x600")
game_canvas = Canvas(game_window)

game_canvas["bg"] = "red"

mouse = Mouse(game_window)
keyboard = Keyboard(game_window)

mouse_shape = circle
mouse_shape.options["fill"] = ""
mouse_shape.options["dash"] = 1
mouse_shape.options["outline"] = "black"
mouse_object = Object(game_canvas, (0, 0), mouse_shape)

keyboard_shape = square
keyboard_shape.options["fill"] = ""
keyboard_shape.options["dash"] = 1
keyboard_shape.options["outline"] = "black"
keyboard_object = Object(game_canvas, (0, 0), keyboard_shape)


def follow_mouse(e):
    mouse_object.position = (e.x, e.y)
    mouse_object.update_shape()


def on_click(e):
    Object(game_canvas, (e.x, e.y), square)


def move_left(e):
    keyboard_object.position = (keyboard_object.position[0] - 10, keyboard_object.position[1])
    keyboard_object.draw()


def move_right(e):
    keyboard_object.position = (keyboard_object.position[0] + 10, keyboard_object.position[1])
    keyboard_object.draw()


def move_down(e):
    keyboard_object.position = (keyboard_object.position[0], keyboard_object.position[1] + 10)
    keyboard_object.draw()


def move_up(e):
    keyboard_object.position = (keyboard_object.position[0], keyboard_object.position[1] - 10)
    keyboard_object.draw()


mouse.on_move(follow_mouse)
mouse.on_right_click(on_click)

keyboard.on_key_down("w", move_up)
keyboard.on_key_down("a", move_left)
keyboard.on_key_down("s", move_down)
keyboard.on_key_down("d", move_right)

game_window.mainloop()
