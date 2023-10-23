from typing import Callable

from src.core.display.Window import Window
from src.core.input.Keyboard import Keyboard
from src.core.objects.Object import Object


class Movement:
    keyboard: Keyboard = None

    def __init__(
            self, obj: Object, speed: int = 10, collision: bool = True,
            *,
            directions: tuple[bool, bool, bool, bool] = None,
            movable: bool = True,
            movement_keys: dict[str: list[str]] = None,
    ):
        """
        Limited to 1 global keyboard which registers events for the absolute root window!
        ^ Won't fix in the foreseeable future!
        """
        self.object = obj
        self.speed = speed
        self.collision = collision

        if directions is None:
            directions = (True, True, True, True)
        self.directions = directions
        self.movable = movable

        if movement_keys is None:
            movement_keys = {"left": ["a"], "right": ["d"], "up": ["w"], "down": ["s"]}
        self.movement_keys = movement_keys

        if not Movement.keyboard:
            Movement.keyboard = Keyboard(Window.ROOT)

        self.__on_collision = []

        self.add_movement()

    def add_movement(self) -> None:
        for left_key in self.movement_keys["left"]:
            self.keyboard.on_key_down(left_key, self.move_left)
        for right_key in self.movement_keys["right"]:
            self.keyboard.on_key_down(right_key, self.move_right)
        for up_key in self.movement_keys["up"]:
            self.keyboard.on_key_down(up_key, self.move_up)
        for down_key in self.movement_keys["down"]:
            self.keyboard.on_key_down(down_key, self.move_down)

    def move_left(self) -> None:
        if not self.check_collision("left") and self.movable:
            self.object.position = (self.object.position[0] - self.speed, self.object.position[1])
            self.object.update()

    def move_right(self) -> None:
        if not self.check_collision("right") and self.movable:
            self.object.position = (self.object.position[0] + self.speed, self.object.position[1])
            self.object.update()

    def move_up(self) -> None:
        if not self.check_collision("up") and self.movable:
            self.object.position = (self.object.position[0], self.object.position[1] - self.speed)
            self.object.update()

    def move_down(self) -> None:
        if not self.check_collision("down") and self.movable:
            self.object.position = (self.object.position[0], self.object.position[1] + self.speed)
            self.object.update()

    def check_collision(self, direction: str = None):
        if not self.collision:
            return False

        collisions = self.object.check_collision()
        if collisions and self.__on_collision:
            for func in self.__on_collision:
                try:
                    func(self)
                except TypeError:
                    func()

        if direction:
            return direction in collisions
        return collisions

    def disable_movement(self) -> None:
        self.movable = False

    def enable_movement(self) -> None:
        self.movable = True

    def remove_movement(self) -> None:
        for left_key in self.movement_keys["left"]:
            self.keyboard.del_key_down(left_key, self.move_left)
        for right_key in self.movement_keys["right"]:
            self.keyboard.del_key_down(right_key, self.move_right)
        for up_key in self.movement_keys["up"]:
            self.keyboard.del_key_down(up_key, self.move_up)
        for down_key in self.movement_keys["down"]:
            self.keyboard.del_key_down(down_key, self.move_down)

    def on_collision(self, func: Callable):
        self.__on_collision.append(func)

    def del_on_collision(self, func: Callable = None):
        if func is None:
            self.__on_collision = []
        else:
            self.__on_collision.remove(func)
