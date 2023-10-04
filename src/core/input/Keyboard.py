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

    def __init__(self, parent: Canvas | Window):
        super().__init__(parent)

        self.add_event("<KeyPress>", self.__on_key_down)
        self.add_event("<KeyRelease>", self.__on_key_up)

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
        char = e.char + "_down"
        self.keys_pressed[char] = True
        if not self.events.get(char) or not self.keys_pressed.get(char):
            return
        for func in self.events.get(char):
            func(e)

    def __on_key_up(self, e):
        char = e.char + "_up"
        self.keys_pressed[char] = False
        if not self.events.get(char) or not self.keys_pressed.get(char):
            return
        for func in self.events.get(char):
            func(e)
