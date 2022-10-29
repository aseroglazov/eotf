import mediapipe as mp

from .base import AbstractHandGesture
from ..helpers import distance

mp_hands = mp.solutions.hands


class HandbreadthGesture(AbstractHandGesture):
    def __init__(self, hand):
        self.hand = hand

    @classmethod
    def is_shown(cls, hand) -> bool:
        def index_finger_is_straight():
            return distance(
                hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP],
                hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
            ) > distance(
                hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP],
                hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]
            ) + distance(
                hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP],
                hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP]
            )

        def middle_finger_is_straight():
            return distance(
                hand.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
                hand.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
            ) > distance(
                hand.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP],
                hand.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP]
            ) + distance(
                hand.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP],
                hand.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP]
            )

        def ring_finger_is_straight():
            return distance(
                hand.landmark[mp_hands.HandLandmark.RING_FINGER_TIP],
                hand.landmark[mp_hands.HandLandmark.RING_FINGER_MCP]
            ) > distance(
                hand.landmark[mp_hands.HandLandmark.RING_FINGER_MCP],
                hand.landmark[mp_hands.HandLandmark.RING_FINGER_PIP]
            ) + distance(
                hand.landmark[mp_hands.HandLandmark.RING_FINGER_PIP],
                hand.landmark[mp_hands.HandLandmark.RING_FINGER_DIP]
            )

        def pinky_is_straight():
            return distance(
                hand.landmark[mp_hands.HandLandmark.PINKY_TIP],
                hand.landmark[mp_hands.HandLandmark.PINKY_MCP]
            ) > distance(
                hand.landmark[mp_hands.HandLandmark.PINKY_MCP],
                hand.landmark[mp_hands.HandLandmark.PINKY_PIP]
            ) + distance(
                hand.landmark[mp_hands.HandLandmark.PINKY_PIP],
                hand.landmark[mp_hands.HandLandmark.PINKY_DIP]
            )

        return index_finger_is_straight() \
               and middle_finger_is_straight() \
               and ring_finger_is_straight() \
               and pinky_is_straight()
