from random import randint
from tkinter import PhotoImage

from src.core.display.Canvas import Canvas
from src.core.objects.Shape import Shape


class Object:
    object_ids = []

    def __init__(self, parent: Canvas, position: tuple[int, int], shape: Shape = None, img: str = None):
        self.parent = parent
        self.position = position
        self.shape = shape
        self.img = img
        self.__drawn = False

        # Maybe
        # self.init_object(parent, position, *args, **kwargs)

        self.draw()

    def draw(self):
        if self.shape:
            return self.draw_shape()
        elif self.img:
            return self.draw_img()

        raise ValueError("No definition for drawing")

    def draw_shape(self):
        translated_shape = [(x + self.position[0], y + self.position[1]) for x, y in self.shape]
        if not self.__drawn:
            # Create unique tag
            self.__drawn = "object-" + str(randint(1, 100000000000000000))
            while self.__drawn in self.object_ids:
                self.__drawn = "object-" + str(randint(1, 100000000000000000))

            self.parent.create_polygon(translated_shape, tag=self.__drawn, **self.shape.options)
        else:
            self.update_shape()

    def draw_img(self):
        img = PhotoImage(file=self.img)
        self.parent.create_image(self.position[0], self.position[1], image=img)
        # TODO

    def update_shape(self):
        translated_shape = [(x + self.position[0], y + self.position[1]) for x, y in self.shape]

        self.parent.delete(self.__drawn)
        self.parent.create_polygon(translated_shape, tag=self.__drawn, **self.shape.options)

    # def check_collision(self) -> bool:

    def get_position(self) -> tuple[int, int]:
        return self.position

    def set_position(self, position: tuple[int, int]):
        self.position = position


if __name__ == "__main__":
    # Quick tests:
    shape_vertices = ((1, -1), (1, 1), (-1, 1), (-1, -1))

    from tkinter import Tk

    root = Tk()
    canvas = Canvas(root, width=400, height=400)
    canvas.pack()

    square = Shape(shape_vertices, fill="", outline="red", dash=True, joinstyle="round", smooth=True, size=100)

    z = Object(canvas, (200, 200), square)
    z.draw()
    root.mainloop()
