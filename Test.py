from src.core import *
from src.addons import *

game_window = Window(display_fps=True)
game_window.geometry("800x600")
game_canvas = Canvas(game_window)

game_canvas["bg"] = "red"

mouse = Mouse(game_window)
keyboard = Keyboard(game_window)

mouse_shape = star()
mouse_shape.options["fill"] = ""
mouse_shape.options["dash"] = 1
mouse_shape.options["outline"] = "black"
mouse_object = Object(game_canvas, (0, 0), solid=True, shape=mouse_shape)

keyboard_shape = square()
keyboard_shape.options["fill"] = ""
keyboard_shape.options["dash"] = 1
keyboard_shape.options["outline"] = "black"

keyboard_objects = [Object(game_canvas, (0, 0), shape=keyboard_shape)]


def follow_mouse(e):
    mouse_object.position = (e.x, e.y)
    mouse_object.update()


def on_click(e):
    keyboard_objects.append(Object(game_canvas, (e.x, e.y), solid=False, shape=square()))


def move_left():
    for keyboard_object in keyboard_objects:
        if "left" not in keyboard_object.check_collision_with_threshold([0, 10, 10, 10]):
            keyboard_object.position = (keyboard_object.position[0] - 10, keyboard_object.position[1])
            keyboard_object.update()


def move_right():
    for keyboard_object in keyboard_objects:
        if "right" not in keyboard_object.check_collision_with_threshold([10, 0, 10, 10]):
            keyboard_object.position = (keyboard_object.position[0] + 10, keyboard_object.position[1])
            keyboard_object.update()


def move_down():
    for keyboard_object in keyboard_objects:
        if "down" not in keyboard_object.check_collision_with_threshold([10, 10, 0, 10]):
            keyboard_object.position = (keyboard_object.position[0], keyboard_object.position[1] + 10)
            keyboard_object.update()


def move_up():
    for keyboard_object in keyboard_objects:
        if "up" not in keyboard_object.check_collision_with_threshold([10, 10, 10, 0]):
            keyboard_object.position = (keyboard_object.position[0], keyboard_object.position[1] - 10)
            keyboard_object.update()


mouse.on_move(follow_mouse)
mouse.on_right_click(on_click)

keyboard.on_key_down("w", move_up)
keyboard.on_key_down("a", move_left)
keyboard.on_key_down("s", move_down)
keyboard.on_key_down("d", move_right)
keyboard.on_key_down("ctrl", move_right)

keyboard.register_key_combination("<Control-Key><Shift-Key><W><A>", lambda e: print("strg+w"))

Object(game_canvas, (400, 200), shape=circle()).draw()

game_window.mainloop()
