from eotf.domain import ImaginaryLine

from ..hand import Hand
from .basic import BasicMotion
from .motion_settings import DEFAULT_SIZE_OF_INAPPROPRIATE_HAND_SEQUENCE


class DrawLineMotion(BasicMotion):
    @classmethod
    def starts_with(cls, hand: Hand) -> bool:
        return cls.is_index_finger(hand)

    @classmethod
    def is_index_finger(cls, hand: Hand) -> bool:
        return hand.knuckles_are_horizontal() \
               and hand.handbreadth_is_down() \
               and hand.index_finger.is_straight() \
               and not hand.middle_finger.is_straight() \
               and not hand.ring_finger.is_straight() \
               and not hand.pinky.is_straight()

    def consume(self, hand: Hand) -> None:
        if self.side != hand.side:
            return

        if not self.is_index_finger(hand):
            self.count_of_inappropriate_hands += 1
            return

        self.storage.append(hand)
        if len(self.storage) < 2:
            return

        self.active_figures.add(
            ImaginaryLine(
                start_point=self.storage[-1].index_finger.TIP,
                end_point=self.storage[-2].index_finger.TIP
            )
        )

    def is_active(self) -> bool:
        return self.count_of_inappropriate_hands < DEFAULT_SIZE_OF_INAPPROPRIATE_HAND_SEQUENCE
