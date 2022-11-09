from abc import ABC
from typing import Type
from collections import namedtuple
from math import sqrt

import numpy as np


Point3D = namedtuple('Point3D', ['x', 'y', 'z'])


def get_inheritors(cls: Type[ABC]) -> set[Type[ABC]]:
    inheritors = set()
    for subcls in cls.__subclasses__():
        inheritors.add(subcls)
        inheritors.update(get_inheritors(subcls))
    return inheritors


def distance(start: Point3D, stop: Point3D) -> float:
    square = (stop.x - start.x) ** 2 + (stop.y - start.y) ** 2 + (stop.z - start.z) ** 2
    if square <= 0:
        return 0
    return sqrt(square)


def get_angle(angle_side_point_1: Point3D, angular_point: Point3D, angle_side_point_2: Point3D):
    def normalize(base_point, target_point):
        return np.array(target_point) - np.array(base_point)

    normalized_point_1 = normalize(angular_point, angle_side_point_1)
    normalized_point_2 = normalize(angular_point, angle_side_point_2)

    return np.degrees(
        np.arccos(
            np.dot(normalized_point_1, normalized_point_2)
            /
            (np.linalg.norm(normalized_point_1) * np.linalg.norm(normalized_point_2))
        )
    )
