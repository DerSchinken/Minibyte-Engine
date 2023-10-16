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
        if not self.render_definition:
            raise ValueError("No rendering definition defined")

        self._id = self.render_definition.draw(self.position, self._id, self.object_ids, self.parent)

    def update(self):
        self.render_definition.update(self.position, self._id, self.parent)

    def check_collision(self):
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

    def check_collision_with_threshold(
            self, threshold: int | float | list[int, int, int, int] | tuple[int, int, int, int]
    ) -> list[str] | list:
        """
        Check collisions with a threshold
        :param threshold: Can be int, float or a list/tuple which is in [left, right, up, down]
        """
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
        if self._id is not None:
            return self.parent.bbox(self._id)
        else:
            return 0, 0, 0, 0  # Return a default empty bounding box if the ID is not set

    def get_position(self) -> tuple[int, int]:
        return self.position

    def set_position(self, position: tuple[int, int]):
        self.position = position

    def destroy(self):
        Object.all_objects.remove(self)
        self.parent.delete(self._id)
        del self
