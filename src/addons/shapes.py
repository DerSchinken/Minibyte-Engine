from math import tau, cos, sin

from src.core.objects.Shape import Shape


def square() -> Shape:
    square_vertices = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
    return Shape(square_vertices, size=50, fill="black")


def triangle() -> Shape:
    triangle_vertices = [(0, -1), (-1, 1), (1, 1)]
    return Shape(triangle_vertices, size=50, fill="black")


def star() -> Shape:
    star_vertices = [
        (0, -1),
        (0.224, -0.309),
        (0.951, -0.309),
        (0.361, 0.118),
        (0.587, 0.809),
        (0, 0.454),
        (-0.587, 0.809),
        (-0.361, 0.118),
        (-0.951, -0.309),
        (-0.224, -0.309)
    ]
    return Shape(star_vertices, size=50, fill="black")


def circle() -> Shape:
    def get_all_circle_coords(x_center, y_center, radius, n_points):
        # Shamelessly stolen from: https://gis.stackexchange.com/a/395090
        thetas = [i / n_points * tau for i in range(n_points)] # τ
        circle_coordinates = [(radius * cos(theta) + x_center, radius * sin(theta) + y_center) for theta in thetas]
        return circle_coordinates

    # Using the second function to generate all the pairs of coordinates.
    circle_vertices = get_all_circle_coords(x_center=0, y_center=0, radius=1, n_points=500)
    return Shape(circle_vertices, size=50, fill="black")
