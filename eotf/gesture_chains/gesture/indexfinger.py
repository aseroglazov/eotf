from .base import AbstractHandGesture
from .hand_structure import Hand


class DrawingFingerGesture(AbstractHandGesture):
    @classmethod
    def is_shown(cls, hand: Hand) -> bool:
        return hand.knuckles_are_horizontal() \
               and hand.handbreadth_is_down() \
               and hand.index_finger.is_straight() \
               and not hand.middle_finger.is_straight() \
               and not hand.ring_finger.is_straight() \
               and not hand.pinky.is_straight()
