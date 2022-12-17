from eotf.domain.tools import distance
from ..hand import Hand
from .basic import BasicMotion
from .helpers import normalize_start_end_points
from .filtering import FilteringConditions
from .motion_settings import DEFAULT_SIZE_OF_INAPPROPRIATE_HAND_SEQUENCE


class ErasingMotion(BasicMotion):
    @classmethod
    def starts_with(cls, hand: Hand) -> bool:
        return cls.is_handbreadth(hand)

    @classmethod
    def is_handbreadth(cls, hand: Hand) -> bool:
        return hand.index_finger.is_straight() \
               and hand.middle_finger.is_straight() \
               and hand.ring_finger.is_straight() \
               and hand.pinky.is_straight() \
               and distance(hand.index_finger.TIP, hand.middle_finger.PIP) \
               < distance(hand.index_finger.TIP, hand.index_finger.PIP) \
               and distance(hand.pinky.TIP, hand.ring_finger.PIP) \
               < distance(hand.pinky.TIP, hand.pinky.PIP)

    def consume(self, hand: Hand) -> None:
        if self.side != hand.side:
            return

        if not self.is_handbreadth(hand):
            self.count_of_inappropriate_hands += 1
            return

        self.storage.append(hand)
        if len(self.storage) < 2:
            return

        start_point = self.storage[-2].middle_finger.TIP
        end_point = self.storage[-1].wrist
        start_point, end_point = normalize_start_end_points(start_point, end_point)

        figures_to_remove = self.active_figures.filter_by(
            FilteringConditions().area_for_search(start_point, end_point)
        )

        for figure in figures_to_remove:
            self.active_figures.remove(figure)

    def is_active(self) -> bool:
        return self.count_of_inappropriate_hands < DEFAULT_SIZE_OF_INAPPROPRIATE_HAND_SEQUENCE
