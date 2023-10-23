from tkinter import PhotoImage

from src.core.constants import POSITION
from src.core.display.containers.Canvas import Canvas
from src.core.objects.drawables.Drawable import Drawable


class MBEImage(Drawable, PhotoImage):
    __supported_file_types = ["jpg", "jpeg", "png", "gif"]

    def __init__(self, *args, **kwargs):
        potential_file: str = "" if len(args) <= 0 else args[0]
        if potential_file.split(".")[-1] in self.__supported_file_types:
            self.__file = potential_file
            args, kwargs["file"] = args[1:], potential_file

        super().__init__(*args, **kwargs)

    def draw(self, master: Canvas, position: POSITION, object_id: str) -> None:
        master.create_image(position[0], position[1], image=self, tag=object_id)

    def update(self, master: Canvas, position: POSITION, object_id: str) -> None:
        master.delete(object_id)
        master.create_image(position[0], position[1], image=self, tag=object_id)
