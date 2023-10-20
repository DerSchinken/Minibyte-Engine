from src.core import *
from src.std import *

game_window = Window(display_fps=True)
game_window.geometry("800x600")
# game_window.fullscreen()
game_window.disable_alt_f4()
# game_window.always_on_top()
# ^ IMPORTANT: Please make sure to set the taskmanager to always stay on top before testing this!
game_canvas = Canvas(game_window)

game_canvas["bg"] = "red"

mouse = Mouse(game_window)
keyboard = Keyboard(game_window)

mouse_shape = star()
mouse_shape.options["fill"] = ""
mouse_shape.options["dash"] = 1
mouse_shape.options["outline"] = "black"
mouse_object = Object(game_canvas, mouse_shape, (0, 0), solid=False)

keyboard_shape = square()
keyboard_shape.options["fill"] = ""
keyboard_shape.options["dash"] = 1
keyboard_shape.options["outline"] = "black"

keyboard_objects = [Object(game_canvas, keyboard_shape, (0, 0))]


def follow_mouse(e):
    mouse_object.position = (e.x, e.y)
    mouse_object.update()


def on_click(e):
    keyboard_objects.append(Object(game_canvas, star(), (e.x, e.y), solid=False))
    Movement(keyboard_objects[-1])


mouse.on_move(follow_mouse)
mouse.on_right_click(on_click)

Movement(keyboard_objects[-1])

keyboard.register_key_combination("<Control-Key><Shift-Key><W><A>", lambda e: print("strg+w"))

Object(game_canvas, circle(), (400, 200))

test_img = MBEImage("test.png")
Object(game_canvas, test_img, (700, 200))

game_window.mainloop()
