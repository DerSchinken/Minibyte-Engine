from typing import Callable

from src.core.display.containers.Canvas import Canvas
from src.core.display.Window import Window
from src.core.input.InputEvent import InputEvent


class Mouse(InputEvent):
    position = [0, 0]

    def __init__(self, parent: Window | Canvas):
        super().__init__(parent)

        if not self.position[0] and not self.position[1]:
            # ^ To somewhat avoid having multiple default __on_move events when only
            # 1 is needed since the position attribute is shared for all instances
            self.add_event("<Motion>", self.__on_move)

    def on_right_click(self, func: Callable) -> None:
        self.add_event("<Button-1>", func)

    def on_middle_click(self, func: Callable) -> None:
        self.add_event("<Button-2>", func)

    def on_left_click(self, func: Callable) -> None:
        self.add_event("<Button-3>", func)

    def on_scroll_up(self, func: Callable) -> None:
        self.add_event("<Button-4>", func)

    def on_scroll_down(self, func: Callable) -> None:
        self.add_event("<Button-5>", func)

    def on_move(self, func: Callable) -> None:
        self.add_event("<Motion>", func)

    def __on_move(self, e) -> None:
        self.position[0] = e.x
        self.position[1] = e.y
