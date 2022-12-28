from abc import abstractmethod

from numpy import ndarray

from eotf.domain import ActiveImaginaryFigures, DomainHandler

from .hand_detection import HandDetection


class AbstractVideoPresenter:
    @abstractmethod
    def visualize_and_send(self, image: ndarray, figures_to_draw: ActiveImaginaryFigures):
        raise NotImplementedError


class Video2VideoHandler:
    def __init__(self, domain: DomainHandler, presenter: AbstractVideoPresenter):
        self.domain = domain
        self.presenter = presenter

        self.detector = HandDetection(self.domain.hand_implementation)

    def consume(self, frame):
        hands = self.detector.get_hands(frame)
        for hand in hands:
            self.domain.consume(hand)
        self.presenter.visualize_and_send(frame, self.domain.imaginary_figures)
