from src.core.objects.Object import Object
from src.core.display.Window import Window
from src.core.input.Keyboard import Keyboard


class Movement:
    __keyboard = None

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
        self.__object = obj
        self.speed = speed
        self.collision = collision

        if directions is None:
            directions = (True, True, True, True)
        self.directions = directions
        self.movable = movable

        if movement_keys is None:
            movement_keys = {"left": ["a"], "right": ["d"], "up": ["w"], "down": ["s"]}
        self.movement_keys = movement_keys

        if not Movement.__keyboard:
            Movement.__keyboard = Keyboard(Window.ROOT)

        self.add_movement()

    def add_movement(self):
        for left_key in self.movement_keys["left"]:
            self.__keyboard.on_key_down(left_key, self.move_left)
        for right_key in self.movement_keys["right"]:
            self.__keyboard.on_key_down(right_key, self.move_right)
        for up_key in self.movement_keys["up"]:
            self.__keyboard.on_key_down(up_key, self.move_up)
        for down_key in self.movement_keys["down"]:
            self.__keyboard.on_key_down(down_key, self.move_down)

    def move_left(self):
        if ("left" not in self.__object.check_collision() or not self.collision) and self.movable:
            self.__object.position = (self.__object.position[0] - self.speed, self.__object.position[1])
            self.__object.update()

    def move_right(self):
        if ("right" not in self.__object.check_collision() or not self.collision) and self.movable:
            self.__object.position = (self.__object.position[0] + self.speed, self.__object.position[1])
            self.__object.update()

    def move_up(self):
        if ("up" not in self.__object.check_collision() or not self.collision) and self.movable:
            self.__object.position = (self.__object.position[0], self.__object.position[1] - self.speed)
            self.__object.update()

    def move_down(self):
        if ("down" not in self.__object.check_collision() or not self.collision) and self.movable:
            self.__object.position = (self.__object.position[0], self.__object.position[1] + self.speed)
            self.__object.update()

    def disable_movement(self):
        pass  # TODO

    def remove_movement(self):
        pass  # TODO
