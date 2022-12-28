from eotf.domain import ImaginaryRectangle, \
    ActiveImaginaryFigures
from eotf.domain.tools import distance, Point3D
from ..hand import Hand
from .basic import BasicMotion
from .filtering import FilteringConditions
from .helpers import normalize_start_end_points
from .motion_settings import DEFAULT_SIZE_OF_INAPPROPRIATE_HAND_SEQUENCE


def is_grip(hand: Hand) -> bool:
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


class DrawRectangleMotion(BasicMotion):
    @classmethod
    def starts_with(cls, hand: Hand) -> bool:
        return is_grip(hand)

    def consume(self, hand: Hand) -> None:
        if self.side != hand.side:
            return

        if not is_grip(hand):
            self.count_of_inappropriate_hands += 1

        self.storage.append(hand)

        if not self.is_active():
            self.complete_action()

    def complete_action(self) -> None:
        if len(self.storage) < 2:
            return
        start_point = self.storage[0].thumb.TIP
        end_point = Point3D(
            x=self.storage[-1].pinky.TIP.x,
            y=self.storage[-1].middle_finger.TIP.y,
            z=self.storage[-1].pinky.TIP.z
        )
        start_point, end_point = normalize_start_end_points(start_point, end_point)

        interferring_rectangles = self.active_figures.filter_by(
            FilteringConditions().area_for_search(start_point, end_point).instance_of(ImaginaryRectangle)
        )
        if interferring_rectangles:
            return

        self.active_figures.add(
            ImaginaryRectangle(start_point, end_point)
        )

    def is_active(self) -> bool:
        return len(self.storage) < 2 and self.count_of_inappropriate_hands < DEFAULT_SIZE_OF_INAPPROPRIATE_HAND_SEQUENCE


class DragMotion(BasicMotion):
    def __init__(self, active_figures: ActiveImaginaryFigures, hand: Hand):
        super().__init__(active_figures, hand)
        self.grip_rectangles = self._get_rectangles_to_move(hand)

    def _get_rectangles_to_move(self, hand: Hand) -> list[ImaginaryRectangle]:
        start_point = hand.thumb.TIP
        end_point = Point3D(
            x=hand.pinky.TIP.x,
            y=hand.middle_finger.TIP.y,
            z=hand.pinky.TIP.z
        )
        start_point, end_point = normalize_start_end_points(start_point, end_point)

        return self.active_figures.filter_by(
            FilteringConditions().area_for_search(start_point, end_point).instance_of(ImaginaryRectangle)
        )

    @classmethod
    def starts_with(cls, hand: Hand) -> bool:
        return is_grip(hand)

    def consume(self, hand: Hand) -> None:
        if self.side != hand.side:
            return

        if not is_grip(hand):
            self.count_of_inappropriate_hands += 1
            return

        self.storage.append(hand)
        if len(self.storage) < 2:
            return

        self._move_rectangles()

    def _move_rectangles(self) -> None:
        delta_x = self.storage[-1].index_finger.TIP.x - self.storage[-2].index_finger.TIP.x
        delta_y = self.storage[-1].index_finger.TIP.y - self.storage[-2].index_finger.TIP.y

        for rectangle in self.grip_rectangles:
            rectangle.start_point = Point3D(
                x=rectangle.start_point.x + delta_x,
                y=rectangle.start_point.y + delta_y,
                z=rectangle.start_point.z
            )
            rectangle.end_point = Point3D(
                x=rectangle.end_point.x + delta_x,
                y=rectangle.end_point.y + delta_y,
                z=rectangle.end_point.z
            )

    def is_active(self) -> bool:
        return self.count_of_inappropriate_hands < DEFAULT_SIZE_OF_INAPPROPRIATE_HAND_SEQUENCE
