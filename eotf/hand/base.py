from abc import ABC, abstractmethod

from .structure import HandStructure


class AbstractHandGesture(ABC):
    @classmethod
    @abstractmethod
    def is_shown(cls, hand_structure: HandStructure) -> bool:
        raise NotImplementedError


class UnknownHandGesture(AbstractHandGesture):
    @classmethod
    def is_shown(cls, hand_structure: HandStructure) -> bool:
        return False


class NoHandFound(AbstractHandGesture):
    @classmethod
    def is_shown(cls, hand_structure=None) -> bool:
        return False
