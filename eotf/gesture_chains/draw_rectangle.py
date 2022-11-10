from .base import \
    AbstractGestureChain, \
    UpdateOfGestureChain
from .gesture import \
    AbstractHandGesture, \
    GripGesture, \
    DetectedHand
from eotf.figures import \
    ContourRectangle, \
    Figure


class DrawRectangleChain(AbstractGestureChain):
    _chain = [
            GripGesture
        ]

    def __init__(self, hand: DetectedHand) -> None:
        self.received_hands = []
        self.received_hands.append(hand)
        self.quantity_of_empty_gestures = 0
        self.abort_sequence = False

    @property
    def chain(self) -> list[AbstractHandGesture]:
        return self._chain

    @classmethod
    def starts_with(cls, hand_gesture: AbstractHandGesture) -> bool:
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

        return UpdateOfGestureChain(updated, consumed_exclusively)

    @property
    def result(self) -> Figure:
        start_point = self.received_hands[0].hand.thumb.TIP
        end_point = self.received_hands[0].hand.pinky.TIP
        return ContourRectangle(start_point, end_point)

    def is_broken(self) -> bool:
        return self.abort_sequence
