from src.core.constants import POSITION, THRESHOLD
from src.core.display.containers.Canvas import Canvas
from src.core.objects.ObjectManager import ObjectManager
from src.core.objects.drawables.Drawable import Drawable


class Object:
    def __init__(self, parent: Canvas, render_definition: Drawable, position: POSITION, *, solid: bool = True):
        self.parent = parent

        self.render_definition = render_definition
        if not isinstance(self.render_definition, Drawable):
            raise TypeError("'render_definition' is not of type 'Drawable'!")

        self.position = position
        self.solid = solid

        # Create id and add to manager
        self._id: str = ObjectManager.generate_id()
        ObjectManager.object_id_list.append(self._id)
        ObjectManager.object_list.append(self)

        self.draw()

    def draw(self) -> None:
        """
        This draws the object
        Important: Doesn't check if object is off-screen
        :return:
        """
        if not self.render_definition:
            raise ValueError("No rendering definition defined")

        self.render_definition.draw(self.parent, self.position, self._id)

    def update(self) -> None:
        """
        Updates self on the display when in scope of the parent
        """
        if not self._id:
            return self.draw()

        if not self.check_off_screen():
            self.render_definition.update(self.parent, self.position, self._id)

    def check_collision(self, direction: str = None, threshold: THRESHOLD = None) -> bool | list[str]:
        if threshold is None:  # [left, right, up, down]
            threshold = 0
        if not (isinstance(threshold, int) or isinstance(threshold, float)):
            if not (isinstance(threshold, tuple) or isinstance(threshold, list)):
                raise ValueError("Invalid value for 'threshold'")
        else:
            threshold = [threshold] * 4  # FIXME: This isn't working as intended

        directions = []
        for other_object in ObjectManager.object_list:
            if other_object is not self and other_object.solid:
                x1, y1, x2, y2 = self.get_bounding_box()
                x3, y3, x4, y4 = other_object.get_bounding_box()

                if x2 > x3 and x1 < x4 and y2 > y3 and y1 < y4:
                    # Objects are colliding
                    if x2 > x4 and x2 - x4 > threshold[0]:
                        directions.append("left")
                    if x1 < x3 and x3 - x1 > threshold[1]:
                        directions.append("right")
                    if y2 > y4 and y2 - y4 > threshold[2]:
                        directions.append("up")
                    if y1 < y3 and y3 - y1 > threshold[3]:
                        directions.append("down")

        if direction:
            return direction in directions
        return directions

    def get_bounding_box(self) -> tuple[int, int, int, int]:
        """
        Calculate the theoretical bounding box with a new position.
        :return: a tuple of X1, Y1, X2, Y2 coordinates for a rectangle that encloses the object.
        """
        if self._id is not None:
            x1, y1, x2, y2 = self.parent.bbox(self._id)
            width = x2 - x1
            height = y2 - y1
            new_x1 = self.position[0] - width // 2
            new_y1 = self.position[1] - height // 2
            new_x2 = new_x1 + width
            new_y2 = new_y1 + height
            return new_x1, new_y1, new_x2, new_y2
        else:
            return 0, 0, 0, 0  # Return a default empty bounding box if the ID is not set

    def check_off_screen(self, extra: int = 100) -> bool:
        """
        Checks if the object is off_screen
        :return: True when off-screen otherwise False
        """
        object_render_area = self.get_bounding_box()

        parent_size = (self.parent.winfo_width() + extra, self.parent.winfo_height() + extra)
        if object_render_area[0] > parent_size[0] or object_render_area[1] > parent_size[1]:
            return True
        if object_render_area[2] < 0 - extra or object_render_area[3] < 0 - extra:
            return True

        return False

    def get_position(self) -> tuple[int, int]:
        return self.position

    def set_position(self, position: tuple[int, int]):
        self.position = position

    def destroy(self) -> None:
        ObjectManager.object_list.remove(self)
        ObjectManager.object_id_list.remove(self._id)
        self.parent.delete(self._id)
