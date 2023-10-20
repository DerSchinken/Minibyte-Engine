from typing import Callable
from tkinter import Event

from src.core.display.Canvas import Canvas
from src.core.display.Window import Window
from src.core.input.InputEvent import InputEvent


class Keyboard(InputEvent):
    """
    IMPORTANT: This event handler will not work if you use a non focused Canvas,
    so consider using the root window instead of a Canvas
    """
    keys_pressed: dict[str: bool] = {}
    key_combos: list[list[str]] = []

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

    def register_key_combination(self, combination: str, func: Callable) -> None:
        """
        Registers a key combination.
        :param combination: Key combination
        :param func: Function which is triggered on key combo
        :return:
        """
        if "+" in combination:
            _combination = []
            for key in combination.split("+"):
                special_key = self.__sanitize_special_key(key)
                if special_key:
                    _combination.append(special_key)
                else:
                    _combination.append(f"<{key}>")

        self.add_event(combination, func)

    def on_key_down(self, char: str, func: Callable) -> None:
        """
        Adds specific event func to char down event, can also add all event funcs to char down event.
        :param char: Char where event func, is triggered
        :param func: Function which is triggered on char down
        :return:
        """
        special_key = self.__sanitize_special_key(char)
        if special_key:
            char = special_key

        if self.events.get(char):
            self.events[char + "_down"].append(func)
        else:
            self.events[char + "_down"] = [func]

    def del_key_down(self, char: str, func: Callable | str) -> None:
        """
        Removes specific event func from char down event, can also remove all event funcs from char down event.
        :param char: Char where event func, is triggered
        :param func: Function which is triggered on char down
        :return:
        """
        special_key = self.__sanitize_special_key(char)
        if special_key:
            char = special_key

        if func == "*" or func == "all":
            self.events[char + "_down"] = []
        else:
            self.events[char + "_down"].remove(func)

    def on_key_up(self, char: str, func: Callable) -> None:
        """
        Adds specific event func to char up event, can also add all event funcs to char up event.
        :param char: Char where event func, is triggered
        :param func: Function which is triggered on char down
        :return:
        """
        special_key = self.__sanitize_special_key(char)
        if special_key:
            char = special_key

        if self.events.get(char):
            self.events[char + "_up"].append(func)
        else:
            self.events[char + "_up"] = [func]

    def del_key_up(self, char: str, func: Callable | str) -> None:
        """
        Removes specific event func from char up event, can also remove all event funcs from char up event.
        :param char: Char where event func, is triggered
        :param func: Function which is triggered on char down
        :return:
        """
        special_key = self.__sanitize_special_key(char)
        if special_key:
            char = special_key

        if func == "*" or func == "all":
            self.events[char + "_up"] = []
        else:
            self.events[char + "_up"].remove(func)

    def __on_key_down(self, e: Event) -> None:
        char = e.char

        if not self.events.get(char + "_down"):
            special_key = self.__get_special_key(e)
            if special_key and self.events.get(special_key + "_down"):
                char = special_key
            else:
                return

        self.keys_pressed[char] = True

    def __on_key_up(self, e: Event) -> None:
        char = e.char + "_up"

        if not self.events.get(char) or self.keys_pressed.get(char):
            special_key = self.__get_special_key(e)
            char = special_key + "_up"
            if not (special_key and self.events.get(char)):
                self.keys_pressed[char.replace("_up", "")] = False
                return

        self.keys_pressed[char.replace("_up", "")] = False

        for func in self.events.get(char):
            func(e)

    def __key_press_event_loop(self) -> None:
        for pressed_key in self.keys_pressed.keys():
            if self.keys_pressed[pressed_key]:
                for func in self.events.get(pressed_key + "_down"):
                    func()

        self.parent.after(self.event_loop_time, self.__key_press_event_loop)

    @staticmethod
    def __sanitize_special_key(key: str) -> str | bool:
        if key.lower() == "ctrl":
            return "<Control-Key>"
        elif key.lower() == "shift":
            return "<Shift-Key>"
        elif key.lower() == "alt":
            return "<Alt-Key>"
        elif key.lower() == "backspace":
            return "<BackSpace>"

        return False

    def __get_special_key(self, key_event) -> str:
        if str(key_event.keysym).startswith("Control"):
            return self.__sanitize_special_key("ctrl")
        elif str(key_event.keysym).startswith("Shift"):
            return self.__sanitize_special_key("shift")
        elif str(key_event.keysym).startswith("Alt"):
            return self.__sanitize_special_key("alt")
        elif str(key_event.keysym).startswith("BackSpace"):
            return self.__sanitize_special_key("backspace")

        return key_event.char
