from tkinter import PhotoImage

from src.core.constants import POSITION
from src.core.display.Canvas import Canvas
from src.core.objects.drawables.Drawable import Drawable


class MBEImage(Drawable, PhotoImage):
    __supported_file_types = ["jpg", "jpeg", "png", "gif"]

    def __init__(self, file: str, *args, **kwargs):
        if file.split(".")[-1] not in self.__supported_file_types:
            raise TypeError(
                f"'{file}' is of a not supported file type," 
                f" for a list of supported types please look into the documentation!"
            )
        self.__file = file
        super().__init__(file=self.__file, *args, **kwargs)

    def draw(self, master: Canvas, position: POSITION, object_id: str) -> None:
        master.create_image(position[0], position[1], image=self, tag=object_id)

    def update(self, master: Canvas, position: POSITION, object_id: str) -> None:
        master.delete(object_id)
        master.create_image(position[0], position[1], image=self, tag=object_id)
