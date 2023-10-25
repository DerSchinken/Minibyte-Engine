from src.core.objects.Object import Object
from src.core.constants import THRESHOLD


def check_collision(*objects: Object, threshold: THRESHOLD = None, same_parent: bool = True) -> bool:
    """
    Checks for collision between 'objects'
    :param same_parent: Set to false to disable error when objects have different parents
    :param threshold: Threshold for the collisions to be met
    :return: Returns True if at least 1 of the objects collide
    """
    if same_parent:
        for _object in objects:
            _object: Object
            if not _object.parent == objects[0]:
                raise ReferenceError("at least 1 object doesn't have the same parent!")

    amount_of_objects = len(objects)
    for first_object in range(amount_of_objects):
        for second_object in range(first_object + 1, amount_of_objects):
            x1, y1, x2, y2 = objects[first_object].get_bounding_box()
            x3, y3, x4, y4 = objects[second_object].get_bounding_box()

            if x2 > x3 and x1 < x4 and y2 > y3 and y1 < y4:
                # Objects are colliding
                if x2 > x4 and x2 - x4 > threshold[0]:
                    return True
                if x1 < x3 and x3 - x1 > threshold[1]:
                    return True
                if y2 > y4 and y2 - y4 > threshold[2]:
                    return True
                if y1 < y3 and y3 - y1 > threshold[3]:
                    return True

    return False
