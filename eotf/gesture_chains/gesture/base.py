from abc import ABC, abstractmethod

from .hand_structure import Hand


class AbstractHandGesture(ABC):
    @classmethod
    @abstractmethod
    def is_shown(cls, hand_structure: Hand) -> bool:
        raise NotImplementedError


class UnknownHandGesture(AbstractHandGesture):
    @classmethod
    def is_shown(cls, hand_structure: Hand) -> bool:
        return False


class NoHandFound(AbstractHandGesture):
    @classmethod
    def is_shown(cls, hand_structure=None) -> bool:
        return False
