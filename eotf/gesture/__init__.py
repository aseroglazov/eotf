from mediapipe.framework.formats.landmark_pb2 import NormalizedLandmarkList

from eotf.gesture.hand_structure import \
    Finger, \
    Hand
from .base import \
    AbstractHandGesture, \
    UnknownHandGesture, \
    NoHandFound
from .handbreadth import HandbreadthGesture
from .indexfinger import DrawingFingerGesture
from eotf.helpers import \
    get_inheritors, \
    Point3D


QUANTITY_OF_LANDMARKS = 21


class Landmarks:
    def __init__(self, landmarks: NormalizedLandmarkList):
        self._landmarks = landmarks
        self._index = 0

    def __iter__(self):
        for i in range(len(self)):
            landmark = self._landmarks.landmark[i]
            yield Point3D(landmark.x, landmark.y, landmark.z)

    @property
    def raw(self):
        return self._landmarks

    def __len__(self):
        return len(self._landmarks.landmark)

    def __index__(self):
        try:
            landmark = self[self._index]
        except IndexError:
            raise StopIteration()
        self._index += 1
        return landmark

    def __getitem__(self, item):
        landmark = self._landmarks.landmark[item]
        return Point3D(landmark.x, landmark.y, landmark.z)


class HandException(Exception):
    pass


class DetectedHand:
    def __init__(self, side: str, landmarks: tuple[Point3D]):
        if len(landmarks.landmark) != QUANTITY_OF_LANDMARKS:
            raise HandException(
                f'Expected {QUANTITY_OF_LANDMARKS} number of landmark, but got {len(landmarks.landmark)}'
            )
        self.landmarks = Landmarks(landmarks)
        self.hand = Hand(side, tuple(self.landmarks))

    @property
    def side(self):
        return self.hand.side

    @property
    def gesture(self) -> AbstractHandGesture:
        if self.landmarks is None:
            return NoHandFound()

        for cls in get_inheritors(AbstractHandGesture):
            if cls.is_shown(self.hand):
                return cls()

        return UnknownHandGesture()
