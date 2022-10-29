from .base import AbstractGestureChain
from .draw_line import DrawLineChain
from .rubber import RubberChain
from ..helpers import get_inheritors
from ..hand import AbstractHandGesture


def get_all_chain_types() -> list[AbstractGestureChain]:
    return get_inheritors(AbstractGestureChain)


def get_chains_starting_with(hand_gesture: AbstractHandGesture) -> list[AbstractGestureChain]:
    return [cls for cls in get_all_chain_types() if cls.starts_with(hand_gesture)]
