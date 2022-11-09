import cv2
from numpy import ndarray
from abc import abstractmethod, ABC
from collections import namedtuple

from eotf.helpers import Point3D


COLOR = (0, 0, 255)
NO_COLOR = (0, 0, 0)

THICKNESS = 10
FILL = -1

TEXT_FONT = cv2.FONT_HERSHEY_SIMPLEX
TEXT_SCALE = 1
TEXT_THICKNESS = 1


Point2D = namedtuple('Point2D', ['x', 'y'])


def scale_coordinates_to_full_image(point: Point3D, image_height: int, image_width: int) -> Point2D:
    return Point2D(int(point.x * image_width), int(point.y * image_height))


class Figure(ABC):
    @abstractmethod
    def draw_on(self, image: ndarray):
        raise NotImplementedError


class Line(Figure):
    def __init__(self, start_point: Point3D, end_point: Point3D):
        self.start_point = start_point
        self.end_point = end_point

    def draw_on(self, image: ndarray) -> None:
        def scale_coordinates(point: Point3D) -> Point2D:
            image_height, image_width = image.shape[:2]
            return scale_coordinates_to_full_image(point, image_height, image_width)

        cv2.line(
            image,
            scale_coordinates(self.start_point),
            scale_coordinates(self.end_point),
            COLOR,
            THICKNESS
        )


class EmptyRectangle(Figure):
    def __init__(self, start_point: Point3D, end_point: Point3D):
        self.start_point = start_point
        self.end_point = end_point

    def draw_on(self, image: ndarray) -> None:
        def scale_coordinates(point: Point3D) -> Point2D:
            image_height, image_width = image.shape[:2]
            return scale_coordinates_to_full_image(point, image_height, image_width)

        cv2.rectangle(
            image,
            scale_coordinates(self.start_point),
            scale_coordinates(self.end_point),
            NO_COLOR,
            FILL
        )


class Text(Figure):
    def __init__(self, bottom_left_corner_of_text: Point3D, message: str):
        self.start_point = bottom_left_corner_of_text
        self.message = message

    def draw_on(self, image: ndarray) -> None:
        def scale_coordinates(point: Point3D) -> Point2D:
            image_height, image_width = image.shape[:2]
            return scale_coordinates_to_full_image(point, image_height, image_width)

        lineType = 2
        cv2.putText(
            image,
            self.message,
            scale_coordinates(self.start_point),
            TEXT_FONT,
            TEXT_SCALE,
            COLOR,
            TEXT_THICKNESS,
            lineType
        )

    def __str__(self):
        return f'{self.message}'

    def __repr__(self):
        return f'start point: {self.start_point}, message: {self.message}'
