from abc import ABC, abstractmethod


class AbstractHandGesture(ABC):
    @classmethod
    @abstractmethod
    def is_shown(cls, hand) -> bool:
        raise NotImplementedError


class UnknownHandGesture(AbstractHandGesture):
    @classmethod
    def is_shown(cls, hand) -> bool:
        return False


class NoHandFound(AbstractHandGesture):
    @classmethod
    def is_shown(cls, hand=None) -> bool:
        return False
