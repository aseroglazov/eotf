from collections import namedtuple

import cv2
from numpy import ndarray

from eotf.domain import Point3D, ImaginaryLine, ImaginaryRectangle, ActiveImaginaryFigures
from eotf.use_cases.video2video import AbstractVideoPresenter
from .settings import COLOR, THICKNESS

Point2D = namedtuple('Point2D', ['x', 'y'])


class AbstractVideoOutput:
    def send(self, image: ndarray):
        raise NotImplementedError


def scale_coordinates(point: Point3D, image: ndarray) -> Point2D:
    image_height, image_width = image.shape[:2]
    return Point2D(int(point.x * image_width), int(point.y * image_height))


class VideoPresenter(AbstractVideoPresenter):
    def __init__(self, output: AbstractVideoOutput):
        self.output = output
        self.color = COLOR
        self.thickness = THICKNESS

    def draw_line(self, image: ndarray, line: ImaginaryLine):
        cv2.line(
            image,
            scale_coordinates(line.start_point, image),
            scale_coordinates(line.end_point, image),
            self.color,
            self.thickness
        )

    def draw_rectangle(self, image: ndarray, rectangle: ImaginaryRectangle):
        cv2.rectangle(
            image,
            scale_coordinates(rectangle.start_point, image),
            scale_coordinates(rectangle.end_point, image),
            self.color,
            self.thickness
        )

    def visualize_and_send(self, image: ndarray, figures_to_draw: ActiveImaginaryFigures):
        for figure in figures_to_draw:
            match figure:
                case ImaginaryLine():
                    self.draw_line(image, figure)
                case ImaginaryRectangle():
                    self.draw_rectangle(image, figure)
        self.output.send(image)
