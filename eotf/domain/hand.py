from abc import abstractmethod


class AbstractHand:
    @property
    @abstractmethod
    def side(self):
        raise NotImplementedError
