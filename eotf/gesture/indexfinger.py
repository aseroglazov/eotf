from .base import AbstractHandGesture
from eotf.gesture.hand_structure import Hand


class DrawingFingerGesture(AbstractHandGesture):
    @classmethod
    def is_shown(cls, hand: Hand) -> bool:
        return hand.knuckles_are_horizontal() \
               and hand.index_finger.is_straight() \
               and hand.middle_finger.is_crunched() \
               and hand.ring_finger.is_crunched() \
               and hand.pinky.is_crunched()
