from abc import ABC, abstractmethod
from collections import namedtuple

from eotf.gesture import AbstractHandGesture
from eotf.figures import Figure

UpdateOfGestureChain = namedtuple('UpdateOfGestureChain', ['updated', 'consumed_exclusively'])


class AbstractGestureChain(ABC):
    @property
    @abstractmethod
    def chain(self) -> list[AbstractHandGesture]:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def starts_with(cls, hand_gesture: AbstractHandGesture) -> bool:
        raise NotImplementedError

    @abstractmethod
    def is_completed(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def send(self, hand) -> bool:
        raise NotImplementedError

    @property
    @abstractmethod
    def result(self) -> Figure:
        raise NotImplementedError

    @abstractmethod
    def is_broken(self) -> bool:
        raise NotImplementedError
