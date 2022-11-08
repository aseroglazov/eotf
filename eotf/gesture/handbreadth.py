from .base import AbstractHandGesture
from eotf.gesture.hand_structure import HandStructure


class HandbreadthGesture(AbstractHandGesture):
    @classmethod
    def is_shown(cls, hand_structure: HandStructure) -> bool:
        return hand_structure.index_finger.is_straight() \
               and hand_structure.middle_finger.is_straight() \
               and hand_structure.ring_finger.is_straight() \
               and hand_structure.pinky.is_straight()
