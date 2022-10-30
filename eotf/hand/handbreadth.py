import mediapipe as mp

from .base import AbstractHandGesture


mp_hands = mp.solutions.hands


class HandbreadthGesture(AbstractHandGesture):
    @classmethod
    def is_shown(cls, hand) -> bool:
        return hand.index_finger.is_straight() \
               and hand.middle_finger.is_straight() \
               and hand.ring_finger.is_straight() \
               and hand.pinky.is_straight()
