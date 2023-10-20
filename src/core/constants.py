from typing import Union


POSITION = Union[tuple[int, int] | list[int, int]]

VERTICES = Union[tuple[tuple[int, int]] | tuple[list[int, int]] | list[tuple[int, int]] | list[list[int, int]]]

VERTEX = Union[tuple[int, int] | list[int, int]]

THRESHOLD = Union[int | float | list[int, int, int, int] | tuple[int, int, int, int]]
