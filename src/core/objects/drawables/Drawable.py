from abc import ABC, abstractmethod
from src.core.constants import POSITION
from src.core.display.Canvas import Canvas


class Drawable(ABC):
    @abstractmethod
    def draw(self, master, position: POSITION, object_id: str):
        pass

    @abstractmethod
    def update(self, master: Canvas, position: POSITION, object_id: str):
        pass
