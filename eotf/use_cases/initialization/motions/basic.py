from eotf.domain import AbstractMotion, \
    ActiveImaginaryFigures
from ..hand import Hand

class BasicMotion(AbstractMotion):
    def __init__(self, active_figures: ActiveImaginaryFigures, hand: Hand):
        self.active_figures = active_figures
        self._side = hand.side
        self.storage = []

        self.count_of_inappropriate_hands = 0

    @property
    def side(self) -> str:
        return self._side
