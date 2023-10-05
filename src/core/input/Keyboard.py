from typing import Callable

from src.core.display.Canvas import Canvas
from src.core.display.Window import Window
from src.core.input.InputEvent import InputEvent


class Keyboard(InputEvent):
    """
    IMPORTANT: This event handler will not work if you use a non focused Canvas,
    so consider using the root window instead of a Canvas
    """
    keys_pressed = {}
    key_combos = []

    def __init__(self, parent: Canvas | Window, event_loop_time: int = 16):
        """
        :param parent: Parent which this event handler will be attached to
        :param event_loop_time: Event loop repetition time in ms
        """
        super().__init__(parent)

        self.event_loop_time = event_loop_time

        self.add_event("<KeyPress>", self.__on_key_down)
        self.add_event("<KeyRelease>", self.__on_key_up)
        self.parent.after(1, self.__key_press_event_loop)

    def register_key_combination(self, combination: str, func: Callable):
        """
        Registers a key combination.
        :param combination: Key combination
        :param func: Function which is triggered on key combo
        :return:
        """
        self.add_event(combination, func)

    def on_key_down(self, char: str, func: Callable):
        """
        Adds specific event func to char down event, can also add all event funcs to char down event.
        :param char: Char where event func, is triggered
        :param func: Function which is triggered on char down
        :return:
        """
        if self.events.get(char):
            self.events[char + "_down"].append(func)
        else:
            self.events[char + "_down"] = [func]

    def del_key_down(self, char: str, func: Callable | str):
        """
        Removes specific event func from char down event, can also remove all event funcs from char down event.
        :param char: Char where event func, is triggered
        :param func: Function which is triggered on char down
        :return:
        """
        if func == "*" or func == "all":
            self.events[char + "_down"] = []
        else:
            self.events[char + "_down"].remove(func)

    def on_key_up(self, char: str, func: Callable):
        """
        Adds specific event func to char up event, can also add all event funcs to char up event.
        :param char: Char where event func, is triggered
        :param func: Function which is triggered on char down
        :return:
        """
        if self.events.get(char):
            self.events[char + "_up"].append(func)
        else:
            self.events[char + "_up"] = [func]

    def del_key_up(self, char: str, func: Callable | str):
        """
        Removes specific event func from char up event, can also remove all event funcs from char up event.
        :param char: Char where event func, is triggered
        :param func: Function which is triggered on char down
        :return:
        """
        if func == "*" or func == "all":
            self.events[char + "_up"] = []
        else:
            self.events[char + "_up"].remove(func)

    def __on_key_down(self, e):
        # FIXME: This will impact key combinations but for now it will work
        # Possible workaround: separate function for adding key combos and then
        # put it into a list and check if the other key is pressed, no time now tho
        if not self.events.get(e.char + "_down"):
            return

        self.keys_pressed[e.char] = True

    def __on_key_up(self, e):
        char = e.char + "_up"
        self.keys_pressed[e.char] = False

        if not self.events.get(char) or not self.keys_pressed.get(char):
            return
        for func in self.events.get(char):
            func(e)

    def __key_press_event_loop(self):
        for pressed_key in self.keys_pressed.keys():
            if self.keys_pressed[pressed_key]:
                for func in self.events.get(pressed_key + "_down"):
                    func()

        self.parent.after(self.event_loop_time, self.__key_press_event_loop)
