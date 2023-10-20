from tkinter import PhotoImage

from src.core.constants import POSITION
from src.core.display.Canvas import Canvas
from src.core.objects.drawables.Drawable import Drawable


class MBEImage(Drawable, PhotoImage):
    def draw(self, master, position: POSITION, object_id: str):
        pass  # TODO

    def update(self, master: Canvas, position: POSITION, object_id: str):
        pass  # TODO
