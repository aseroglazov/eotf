from .base import \
    AbstractHandGesture, \
    UnknownHandGesture, \
    NoHandFound
from .handbreadth import HandbreadthGesture
from .indexfinger import IndexFingerGesture
from ..helpers import get_inheritors


class Hand:
    def __init__(self, side, landmarks):
        self.side = side
        self.landmarks = landmarks

    @property
    def gesture(self) -> AbstractHandGesture:
        if self.landmarks is None:
            return NoHandFound()

        for cls in get_inheritors(AbstractHandGesture):
            if cls.is_shown(self.landmarks):
                return cls(self.landmarks)

        return UnknownHandGesture(self.landmarks)
