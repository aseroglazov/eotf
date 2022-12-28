from eotf.domain.tools import Point3D


def normalize_start_end_points(start_point: Point3D, end_point: Point3D) -> tuple[Point3D, Point3D]:
    normalized_start_point = Point3D(
        x=min(start_point.x, end_point.x),
        y=min(start_point.y, end_point.y),
        z=min(start_point.z, end_point.z)
    )
    normalized_end_point = Point3D(
        x=max(start_point.x, end_point.x),
        y=max(start_point.y, end_point.y),
        z=max(start_point.z, end_point.z)
    )
    return normalized_start_point, normalized_end_point


def is_in_rectangle(rectangle: tuple[Point3D, Point3D], point: Point3D):
    start_point, end_point = rectangle
    if min(start_point.x, end_point.x) < point.x < max(start_point.x, end_point.x) \
            and min(start_point.y, end_point.y) < point.y < max(start_point.y, end_point.y):
        return True
    return False


def rectangles_has_interceptions(rectangle_1: tuple[Point3D, Point3D], rectangle_2: tuple[Point3D, Point3D]) -> bool:
    def get_rectangle_important_points(start_point: Point3D, end_point: Point3D):
        A = Point3D(
            x=min(start_point.x, end_point.x),
            y=min(start_point.y, end_point.y),
            z=min(start_point.z, end_point.z)
        )
        B = Point3D(
            x=max(start_point.x, end_point.x),
            y=min(start_point.y, end_point.y),
            z=min(start_point.z, end_point.z)
        )
        C = Point3D(
            x=max(start_point.x, end_point.x),
            y=max(start_point.y, end_point.y),
            z=max(start_point.z, end_point.z)
        )
        D = Point3D(
            x=min(start_point.x, end_point.x),
            y=max(start_point.y, end_point.y),
            z=max(start_point.z, end_point.z)
        )

        center = Point3D(
            x=A.x + (C.x - A.x) / 2,
            y=A.y + (C.y - A.y) / 2,
            z=A.z + (C.z - A.z) / 2,
        )

        return A, B, C, D, center
    important_points_1 = get_rectangle_important_points(*rectangle_1)
    important_points_2 = get_rectangle_important_points(*rectangle_2)

    if any([is_in_rectangle(rectangle_1, point) for point in important_points_2]) \
            or any([is_in_rectangle(rectangle_2, point) for point in important_points_1]):
        return True
    return False
