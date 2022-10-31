import mediapipe as mp

from .base import AbstractHandGesture
from .structure import HandStructure


mp_hands = mp.solutions.hands


class IndexFingerGesture(AbstractHandGesture):
    @classmethod
    def is_shown(cls, hand_structure: HandStructure) -> bool:
        return hand_structure.index_finger.is_straight() \
               and hand_structure.middle_finger.is_crunched() \
               and hand_structure.ring_finger.is_crunched() \
               and hand_structure.pinky.is_crunched()
