from typing import Type

from .base import AbstractGestureChain
from .draw_line import DrawLineChain
from .rubber import RubberChain
from .draw_rectangle import DrawRectangleChain
from eotf.helpers import get_inheritors
from .gesture import \
    AbstractHandGesture, \
    DetectedHand


__all__ = [
    'AbstractGestureChain',
    'DrawLineChain',
    'RubberChain',
    'DetectedHand',
    'DrawRectangleChain',
    'get_all_chain_types'
]


def get_all_chain_types() -> list[Type[AbstractGestureChain]]:
    return get_inheritors(AbstractGestureChain)


def get_chains_starting_with(hand_gesture: AbstractHandGesture) -> list[AbstractGestureChain]:
    return [cls for cls in get_all_chain_types() if cls.starts_with(hand_gesture)]
