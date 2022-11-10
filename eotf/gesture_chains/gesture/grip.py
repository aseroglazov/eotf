from .base import AbstractHandGesture
from .hand_structure import Hand
from eotf.helpers import distance


class GripGesture(AbstractHandGesture):
    @classmethod
    def is_shown(cls, hand: Hand) -> bool:
        return hand.knuckles_are_horizontal() \
               and hand.handbreadth_is_down() \
               and hand.index_finger.is_straight() \
               and hand.middle_finger.is_straight() \
               and hand.ring_finger.is_straight() \
               and hand.pinky.is_straight() \
               and distance(hand.index_finger.TIP, hand.middle_finger.PIP) \
                    > distance(hand.index_finger.TIP, hand.index_finger.PIP) \
               and distance(hand.pinky.TIP, hand.ring_finger.PIP) \
                    > distance(hand.pinky.TIP, hand.pinky.PIP)
