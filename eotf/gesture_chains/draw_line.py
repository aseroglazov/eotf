import mediapipe as mp
from typing import Type

from .base import \
    AbstractGestureChain, \
    UpdateOfGestureChain
from eotf.figures import \
    Line, \
    Figure
from eotf.gesture import \
    AbstractHandGesture, \
    DrawingFingerGesture, \
    DetectedHand


mp_hands = mp.solutions.hands


class DrawLineChain(AbstractGestureChain):
    _chain = [
            DrawingFingerGesture,
            DrawingFingerGesture
        ]
    max_empty_gestures = 10

    def __init__(self, hand) -> None:
        self.received_hands = []
        self.received_hands.append(hand)
        self.quantity_of_empty_gestures = 0
        self.abort_sequence = False

    @property
    def chain(self) -> list[Type[AbstractHandGesture]]:
        return self._chain

    @classmethod
    def starts_with(cls, hand_gesture: Type[AbstractHandGesture]) -> bool:
        return type(hand_gesture) is cls._chain[0]

    def is_completed(self) -> bool:
        return len(self.received_hands) == len(self.chain)

    def send(self, hand: DetectedHand) -> UpdateOfGestureChain:
        updated = False
        consumed_exclusively = False
        index = 0
        if len(self.received_hands):
            index = len(self.received_hands) - 1

        if len(self.chain) > index:
            if type(hand.gesture) is self.chain[index]:
                self.received_hands.append(hand)
                updated = True
                consumed_exclusively = False
                self.quantity_of_empty_gestures = 0
            else:
                self.quantity_of_empty_gestures += 1
                if self.quantity_of_empty_gestures >= self.max_empty_gestures:
                    self.abort_sequence = True

        return UpdateOfGestureChain(updated, consumed_exclusively)

    @property
    def result(self) -> Figure:
        start_point = self.received_hands[0].hand.index_finger.TIP
        end_point = self.received_hands[1].hand.index_finger.TIP
        return Line(start_point, end_point)

    def is_broken(self) -> bool:
        return self.abort_sequence
