from abc import ABC, abstractmethod


class AbstractHandGesture(ABC):
    @classmethod
    @abstractmethod
    def is_shown(cls, hand) -> bool:
        raise NotImplementedError


class UnknownHandGesture(AbstractHandGesture):
    def __init__(self, hand):
        self.hand = hand

    @classmethod
    def is_shown(cls, hand) -> bool:
        return False


class NoHandFound(AbstractHandGesture):
    def __init__(self, hand=None):
        self.hand = hand

    @classmethod
    def is_shown(cls, hand=None) -> bool:
        return False
