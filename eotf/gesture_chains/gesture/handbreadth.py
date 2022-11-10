from .base import AbstractHandGesture
from .hand_structure import Hand


class HandbreadthGesture(AbstractHandGesture):
    @classmethod
    def is_shown(cls, hand: Hand) -> bool:
        return hand.index_finger.is_straight() \
               and hand.middle_finger.is_straight() \
               and hand.ring_finger.is_straight() \
               and hand.pinky.is_straight()
