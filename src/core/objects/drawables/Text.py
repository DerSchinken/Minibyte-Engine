from src.core.constants import POSITION, FONT
from src.core.display.containers.Canvas import Canvas
from src.core.objects.drawables.Drawable import Drawable


class Text(Drawable):
    def __init__(self, text: str, fill: str = "black", font: FONT = ("Arial", 14), background: str = None):
        """
        :param font: tuple of
        """
        self.__text = text
        self.__fill = fill

        self.check_font(font)
        self.__font = font

        self.__background = background

    def draw(self, master: Canvas, position: POSITION, object_id: str):
        # noinspection PyArgumentList
        master.create_text(
            position[0], position[1],
            text=self.__str__(),
            tag=object_id,
            fill=self.__fill,
            font=self.__font,
        )
        self.__draw_background(master, object_id)

    def update(self, master: Canvas, position: POSITION, object_id: str):
        master.delete(object_id)
        # noinspection PyArgumentList
        master.create_text(
            position[0], position[1],
            text=self.__str__(),
            tag=object_id,
            fill=self.__fill,
            font=self.__font
        )
        self.__draw_background(master, object_id)

    def __draw_background(self, master: Canvas, object_id: str):
        if self.__background:
            master.delete(object_id+"-bg")
            # noinspection PyArgumentList
            master.create_rectangle(master.bbox(object_id), fill=self.__background, tag=object_id+"-bg")
            master.tag_lower(object_id+"-bg", object_id)

    def config(self, text: str = None, fill: str = None, font: FONT = None, background: str = None):
        if text:
            self.__text = text
        if fill:
            self.__fill = fill
        if font:
            self.check_font(font)
            self.__font = font
        if background:
            self.__background = background

    @staticmethod
    def check_font(font: FONT) -> bool:
        """
        Checks if 'font' is in a correct format and raises TypeError if not else it returns True
        :return: True if all checks have passed
        """
        if not isinstance(font, tuple) and not isinstance(font, list):
            raise TypeError("'font' needs to be iterable!")
        if not isinstance(font[0], str):
            raise TypeError("First element of 'font' needs to be of type 'str'!")
        if not isinstance(font[1], int):
            raise TypeError("Second element of 'font' needs to be of type 'int'!")

        return True

    def __str__(self):
        return self.__text
