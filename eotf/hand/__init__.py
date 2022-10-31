from mediapipe.framework.formats.landmark_pb2 import NormalizedLandmarkList
from mediapipe.python.solutions.hands import HandLandmark

from .structure import \
    Finger, \
    HandStructure
from .base import \
    AbstractHandGesture, \
    UnknownHandGesture, \
    NoHandFound
from .handbreadth import HandbreadthGesture
from .indexfinger import IndexFingerGesture
from eotf.helpers import get_inheritors


class Hand:
    def __init__(self, side: str, landmarks: NormalizedLandmarkList):
        self.side = side
        self.landmarks = landmarks
        self.structure = HandStructure(self.landmarks)

    @property
    def gesture(self) -> AbstractHandGesture:
        if self.landmarks is None:
            return NoHandFound()

        for cls in get_inheritors(AbstractHandGesture):
            if cls.is_shown(self.structure):
                return cls()

        return UnknownHandGesture()
