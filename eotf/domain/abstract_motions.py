from abc import abstractmethod

from .imaginary_figures import ActiveImaginaryFigures
from .hand import AbstractHand


class AbstractMotion:
    @abstractmethod
    def __init__(self, active_figures: ActiveImaginaryFigures, hand: AbstractHand):
        raise NotImplementedError

    @property
    @abstractmethod
    def side(self):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def starts_with(cls, hand: AbstractHand) -> bool:
        raise NotImplementedError

    @abstractmethod
    def consume(self, hand: AbstractHand) -> None:
        raise NotImplementedError

    @abstractmethod
    def is_active(self) -> bool:
        raise NotImplementedError

    def __eq__(self, other):
        return type(self) == type(other) and self.side == other.side


class ActiveMotions:
    def __init__(self):
        self._storage = []
        self._index = 0

    def __iter__(self):
        for i in range(len(self)):
            yield self._storage[i]

    def __len__(self):
        return len(self._storage)

    def __index__(self):
        try:
            element = self[self._index]
        except IndexError:
            raise StopIteration()
        self._index += 1
        return element

    def __getitem__(self, index: int):
        return self._storage[index]

    def __contains__(self, item: AbstractMotion):
        for i in self:
            if i == item:
                return True
        return False

    def add(self, item: AbstractMotion):
        if item in self:
            raise AttributeError
        self._storage.append(item)

    def cleanup(self):
        self._storage = [item for item in self._storage if item.is_active()]
