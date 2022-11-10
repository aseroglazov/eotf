from abc import ABC, abstractmethod

from .hand_structure import Hand


class AbstractHandGesture(ABC):
    @classmethod
    @abstractmethod
    def is_shown(cls, hand: Hand) -> bool:
        raise NotImplementedError


class UnknownHandGesture(AbstractHandGesture):
    @classmethod
    def is_shown(cls, hand: Hand) -> bool:
        return False


class NoHandFound(AbstractHandGesture):
    @classmethod
    def is_shown(cls, hand=None) -> bool:
        return False
