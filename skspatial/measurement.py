"""Measurements using spatial objects."""

from dpcontracts import require, ensure

from skspatial.objects import Point, Vector


@require(
    "The inputs must be three points.",
    lambda args: all(
        isinstance(x, Point) for x in [args.point_a, args.point_b, args.point_c]
    ),
)
@ensure("The output must be a float.", lambda _, result: isinstance(result, float))
def area_triangle(point_a, point_b, point_c):
    """
    Return the area of a triangle defined by three points.

    The points are the three vertices of the triangle.

    Parameters
    ----------
    point_a, point_b, point_c : Point
        Input points.

    Returns
    -------
    number
        The area of the triangle.

    Examples
    --------
    >>> from skspatial.objects import Point

    >>> area_triangle(Point([0, 0]), Point([0, 1]), Point([1, 0]))
    0.5

    >>> area_triangle(Point([0, 0]), Point([0, 2]), Point([1, 1]))
    1.0

    References
    ----------
    http://mathworld.wolfram.com/TriangleArea.html

    """
    vector_ab = Vector.from_points(point_a, point_b)
    vector_ac = Vector.from_points(point_a, point_c)

    vector_cross = vector_ab.cross(vector_ac)

    return 0.5 * vector_cross.magnitude