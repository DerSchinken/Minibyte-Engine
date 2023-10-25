from abc import ABC, abstractmethod

from src.core.constants import POSITION
from src.core.display.containers.Canvas import Canvas


class Drawable(ABC):
    @abstractmethod
    def draw(self, parent: Canvas, position: POSITION, object_id: str):
        pass

    @abstractmethod
    def update(self, parent: Canvas, position: POSITION, object_id: str):
        pass
