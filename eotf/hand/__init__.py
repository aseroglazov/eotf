from mediapipe.framework.formats.landmark_pb2 import NormalizedLandmarkList

from .structure import \
    Finger, \
    HandStructure
from .base import \
    AbstractHandGesture, \
    UnknownHandGesture, \
    NoHandFound
from .handbreadth import HandbreadthGesture
from .indexfinger import IndexFingerGesture
from eotf.helpers import \
    get_inheritors, \
    Point3D


QUANTITY_OF_LANDMARKS = 21


class HandException(Exception):
    pass


class Hand:
    def __init__(self, side: str, landmarks: NormalizedLandmarkList):
        self.side = side
        self.raw_landmarks = landmarks
        self.landmarks = None
        self._initialize_landmarks(landmarks)
        self.structure = HandStructure(self.landmarks)

    def _initialize_landmarks(self, landmarks: NormalizedLandmarkList):
        received_dots = []
        if len(landmarks.landmark) != QUANTITY_OF_LANDMARKS:
            raise HandException(f'Expected {QUANTITY_OF_LANDMARKS} number of landmark, but got {len(landmarks.landmark)}')
        for i in range(len(landmarks.landmark)):
            landmark = landmarks.landmark[i]
            received_dots.append(
                Point3D(landmark.x, landmark.y, landmark.z)
            )

        self.landmarks = tuple(received_dots)


    @property
    def gesture(self) -> AbstractHandGesture:
        if self.landmarks is None:
            return NoHandFound()

        for cls in get_inheritors(AbstractHandGesture):
            if cls.is_shown(self.structure):
                return cls()

        return UnknownHandGesture()
