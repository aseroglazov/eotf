from .base import AbstractHandGesture
from .hand_structure import Hand


class HandbreadthGesture(AbstractHandGesture):
    @classmethod
    def is_shown(cls, hand_structure: Hand) -> bool:
        return hand_structure.index_finger.is_straight() \
               and hand_structure.middle_finger.is_straight() \
               and hand_structure.ring_finger.is_straight() \
               and hand_structure.pinky.is_straight()
