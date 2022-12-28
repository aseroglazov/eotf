from .imaginary_figures import ActiveImaginaryFigures
from .abstract_motions import ActiveMotions, AbstractMotion
from .hand import AbstractHand


class DomainHandler:
    def __init__(self, active_imaginary_figures: ActiveImaginaryFigures):
        self._hand_implementation = AbstractHand

        self.active_imaginary_figures = active_imaginary_figures
        self.known_motions = set()
        self._active_motions = ActiveMotions()

    @property
    def active_motions(self):
        self._active_motions.cleanup()
        return self._active_motions

    @property
    def imaginary_figures(self):
        return self.active_imaginary_figures

    @property
    def hand_implementation(self):
        return self._hand_implementation

    @hand_implementation.setter
    def hand_implementation(self, hand_cls: AbstractHand):
        if not issubclass(hand_cls, AbstractHand):
            raise TypeError(f'Class {hand_cls} isn\'t a subclass of {AbstractHand}')
        self._hand_implementation = hand_cls

    def consume(self, hand: AbstractHand):
        for active_motion in self.active_motions:
            active_motion.consume(hand)

        for known_motion in self.known_motions:
            if not known_motion.starts_with(hand):
                continue
            motion = known_motion(self.active_imaginary_figures, hand)
            if motion not in self.active_motions:
                self.active_motions.add(motion)

    def add_known_motion(self, motion: AbstractMotion):
        self.known_motions.add(motion)
