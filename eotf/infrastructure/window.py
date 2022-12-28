import cv2
from numpy import ndarray

from eotf.controllers import AbstractVideoOutput


class WindowVideoOutput(AbstractVideoOutput):
    def send(self, frame: ndarray):
        cv2.imshow('Explain on the fingers', frame)
