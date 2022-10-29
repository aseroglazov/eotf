import mediapipe as mp

mp_hands = mp.solutions.hands

from .base import AbstractGestureChain, UpdateOfGestureChain
from ..hand import AbstractHandGesture, HandbreadthGesture
from ..figures import EmptyRectangle


class RubberChain(AbstractGestureChain):
    _chain = [
            HandbreadthGesture,
            HandbreadthGesture
        ]
    max_empty_gestures = 10

    def __init__(self, hand_gesture: AbstractHandGesture) -> None:
        self.received_gestures = []
        self.received_gestures.append(hand_gesture)
        self.quantity_of_empty_gestures = 0
        self.abort_sequence = False

    @property
    def chain(self) -> list:
        return self._chain

    @classmethod
    def starts_with(cls, hand_gesture: AbstractHandGesture) -> bool:
        return type(hand_gesture) is cls._chain[0]

    def is_completed(self) -> bool:
        return len(self.received_gestures) == len(self.chain)

    def send(self, hand_gesture: AbstractHandGesture) -> None:
        updated = False
        consumed_exclusively = False
        index = 0
        if len(self.received_gestures):
            index = len(self.received_gestures) - 1

        if len(self.chain) > index:
            if type(hand_gesture) is self.chain[index]:
                self.received_gestures.append(hand_gesture)
                updated = True
                consumed_exclusively = False
                self.quantity_of_empty_gestures = 0
            else:
                self.quantity_of_empty_gestures += 1
                if self.quantity_of_empty_gestures >= self.max_empty_gestures:
                    self.abort_sequence = True

        return UpdateOfGestureChain(updated, consumed_exclusively)

    @property
    def result(self):
        start_point = self.received_gestures[0].hand.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        end_point = self.received_gestures[1].hand.landmark[mp_hands.HandLandmark.WRIST]
        return EmptyRectangle(start_point, end_point)

    def is_broken(self):
        return self.abort_sequence
