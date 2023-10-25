from typing import Iterator

from src.core.constants import VERTICES, VERTEX, POSITION
from src.core.display.containers.Canvas import Canvas
from src.core.objects.drawables.Drawable import Drawable


class Shape(Drawable):
    # https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/create_polygon.html
    def __init__(self, shape_vertices: VERTICES, *, size: int | VERTEX = None, **options):
        """
        :param shape_vertices: The vertices from the shape
        :param options: For description please look in the documentation
        """
        self.original_vertices = shape_vertices
        self.vertices = shape_vertices
        if isinstance(size, int):
            size = [size, size]
        self.size = size
        self.options = options

        self.check_vertices(self.vertices, True)

        if self.size:
            self.update_size()

    def draw(self, parent: Canvas, position: POSITION, object_id: str) -> None:
        translated_shape = [(x + position[0], y + position[1]) for x, y in self]
        # noinspection PyArgumentList
        parent.create_polygon(translated_shape, tag=object_id, **self.options)

    def update(self, parent: Canvas, position: POSITION, object_id: str) -> None:
        translated_shape = [(x + position[0], y + position[1]) for x, y in self]

        parent.delete(object_id)
        # noinspection PyArgumentList
        parent.create_polygon(translated_shape, tag=object_id, **self.options)

    @staticmethod
    def check_vertices(vertices: VERTICES, exceptions: bool = False) -> bool:
        """
        Every vertex needs 2 values (x, y) and cant have more than 2
        :raise: ValueError
        :return: None
        """
        for vertex in vertices:
            if len(vertex) < 2:
                if exceptions:
                    raise ValueError("Invalid vertices, need at least 2 values per vertex")
                return False
            elif len(vertex) > 2:
                if exceptions:
                    raise ValueError("Invalid vertices, too many values! At most 2 values per vertex")
                return False

        return True

    def update_size(self) -> None:
        adjusted = []
        for x, y in self.original_vertices:
            if isinstance(self.size, tuple) or isinstance(self.size, list):
                adjusted.append((x * self.size[0], y * self.size[1]))
            else:
                adjusted.append((x * self.size, y * self.size))

        self.vertices = adjusted

    def __getitem__(self, item: int) -> VERTEX:
        return self.vertices[item]

    def __setitem__(self, item: int, value: VERTEX):
        self.check_vertices([value], True)
        self.vertices[item] = value

    def __iter__(self) -> Iterator[int]:
        for vert in self.vertices:
            yield vert

    def __len__(self) -> int:
        return len(self.vertices)
