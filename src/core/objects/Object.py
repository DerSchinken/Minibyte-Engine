from src.core.display.Canvas import Canvas
from src.core.objects.MBEImage import MBEImage
from src.core.objects.Shape import Shape


class Object:
    object_ids = []
    all_objects = []

    def __init__(self, parent: Canvas, position: tuple[int, int], *, solid: bool = True, shape: Shape = None,
                 img: MBEImage = None):
        self.parent = parent
        self.position = position
        self._id = False
        self.solid = solid

        if shape:
            self.render_definition = shape
        elif img:
            self.render_definition = img

        # Maybe
        # self.init_object(parent, position, *args, **kwargs)
        Object.all_objects.append(self)

        self.draw()

    def draw(self):
        """
        This draws the object
        Important: Doesn't check if object is off-screen
        :return:
        """
        if not self.render_definition:
            raise ValueError("No rendering definition defined")

        self._id = self.render_definition.draw(self.position, self._id, self.object_ids, self.parent)

    def update(self):
        """
        Updates self on the display when in scope of the parent
        """
        if not self._id:
            return self.draw()

        if not self.check_off_screen():
            self.render_definition.update(self.position, self._id, self.parent)

    def check_collision(self, threshold: int | float | list[int, int, int, int] | tuple[int, int, int, int] = None):
        if threshold is None:
            threshold = 0
        if not (isinstance(threshold, int) or isinstance(threshold, float)):
            if not (isinstance(threshold, tuple) or isinstance(threshold, list)):
                raise ValueError("Invalid value for 'threshold'")
        else:
            threshold = [threshold] * 4  # TODO

        directions = []
        for other_object in Object.all_objects:
            if other_object is not self and other_object.solid:
                x1, y1, x2, y2 = self.get_bounding_box()
                x3, y3, x4, y4 = other_object.get_bounding_box()

                if x2 > x3 and x1 < x4 and y2 > y3 and y1 < y4:
                    # Objects are colliding
                    if x2 > x4:
                        directions.append("left")
                    if x1 < x3:
                        directions.append("right")
                    if y2 > y4:
                        directions.append("up")
                    if y1 < y3:
                        directions.append("down")

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
            new_x1 = self.position[0] - width//2
            new_y1 = self.position[1] - height//2
            new_x2 = new_x1 + width
            new_y2 = new_y1 + height
            return new_x1, new_y1, new_x2, new_y2
        else:
            return 0, 0, 0, 0  # Return a default empty bounding box if the ID is not set

    def check_off_screen(self, extra: int = 100):
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

    def destroy(self):
        Object.all_objects.remove(self)
        self.parent.delete(self._id)
        del self
