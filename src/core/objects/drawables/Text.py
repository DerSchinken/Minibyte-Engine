from src.core.constants import POSITION
from src.core.display.containers.Canvas import Canvas
from src.core.objects.drawables.Drawable import Drawable


class Text(Drawable):
    def __init__(self, text: str, *cnf, **kwcnf):
        self.cnf = cnf
        self.kwcnf = kwcnf
        self.text = text

    def draw(self, master: Canvas, position: POSITION, object_id: str):
        master.create_text(position[0], position[1], text=self.__str__(), tag=object_id)

    def update(self, master: Canvas, position: POSITION, object_id: str):
        master.delete(object_id)
        master.create_text(position[0], position[1], text=self.__str__(), tag=object_id)

    def __str__(self):
        return self.text
