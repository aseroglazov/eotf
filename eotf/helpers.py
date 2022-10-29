from abc import ABC
from typing import Type
from collections import namedtuple
from math import sqrt


Point3D = namedtuple('Point3D', ['x', 'y', 'z'])
Point2D = namedtuple('Point2D', ['x', 'y'])
DetectedHands = namedtuple('DetectedHands', ['right', 'left'])


class Scene:
    def __init__(self, image):
        self.image = image
        self.detected_objects = []


def get_inheritors(cls: Type[ABC]) -> set[Type[ABC]]:
    inheritors = set()
    for subcls in cls.__subclasses__():
        inheritors.add(subcls)
        inheritors.update(get_inheritors(subcls))
    return inheritors


def scale_coordinates_to_full_image(point: Point3D, image_height: int, image_width: int) -> Point2D:
    return Point2D(int(point.x * image_width), int(point.y * image_height))


def distance(start, stop):
    square = (stop.x - start.x) ** 2 + (stop.y - start.y) ** 2 + (stop.z - start.z) ** 2
    if square <= 0:
        return 0
    return sqrt(square)
