import cv2

from abc import abstractmethod, ABC

from eotf.helpers import Point3D, Point2D, scale_coordinates_to_full_image


COLOR = (0, 0, 255)
NO_COLOR = (0, 0, 0)

THICKNESS = 10
FILL = -1


class Figure(ABC):
    @abstractmethod
    def draw_on(self, image):
        raise NotImplementedError


class Line(Figure):
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def draw_on(self, image):
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
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def draw_on(self, image):
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
