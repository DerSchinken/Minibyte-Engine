from math import tau, cos, sin

from src.core.objects.Shape import Shape

square_vertices = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
square = Shape(square_vertices, size=50, fill="black")

triangle_vertices = [(0, -1), (-1, 1), (1, 1)]
triangle = Shape(triangle_vertices, size=50, fill="black")


def get_all_circle_coords(x_center, y_center, radius, n_points):
    thetas = [i / n_points * tau for i in range(n_points)]
    circle_coords = [(radius * cos(theta) + x_center, radius * sin(theta) + y_center) for theta in thetas]
    return circle_coords


# Using the second function to generate all the pairs of coordinates.
circle_vertices = get_all_circle_coords(x_center=0, y_center=0, radius=1, n_points=500)
circle = Shape(circle_vertices, size=50, fill="black")
