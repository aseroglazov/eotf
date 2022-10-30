from .finger import Finger
from .base import \
    AbstractHandGesture, \
    UnknownHandGesture, \
    NoHandFound
from .handbreadth import HandbreadthGesture
from .indexfinger import IndexFingerGesture
from ..helpers import get_inheritors


FINGER_OFFSET = {
    'THUMB': 1,
    'INDEX_FINGER': 5,
    'MIDDLE_FINGER': 9,
    'RING_FINGER': 13,
    'PINKY': 17
}


class Hand:
    def __init__(self, side, landmarks):
        self.side = side
        self.landmarks = landmarks

        self.thumb = Finger(self._get_finger_landmarks('THUMB'))
        self.index_finger = Finger(self._get_finger_landmarks('INDEX_FINGER'))
        self.middle_finger = Finger(self._get_finger_landmarks('MIDDLE_FINGER'))
        self.ring_finger = Finger(self._get_finger_landmarks('RING_FINGER'))
        self.pinky = Finger(self._get_finger_landmarks('PINKY'))

    def _get_finger_landmarks(self, finger_name):
        finger_landmarks = []
        initial_offset = FINGER_OFFSET[finger_name.upper()]
        for index in range(initial_offset, initial_offset + 4):
            finger_landmarks.append(self.landmarks.landmark[index])

        return finger_landmarks

    @property
    def gesture(self) -> AbstractHandGesture:
        if self.landmarks is None:
            return NoHandFound()

        for cls in get_inheritors(AbstractHandGesture):
            if cls.is_shown(self):
                return cls()

        return UnknownHandGesture()
