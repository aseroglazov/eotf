from abc import ABC, abstractmethod


class AbstractPlugin(ABC):
    @abstractmethod
    def deal_with(self, scene):
        raise NotImplementedError

    @abstractmethod
    def close(self):
        raise NotImplementedError


class BasePlugin(AbstractPlugin):
    def deal_with(self, scene):
        return scene

    def close(self):
        pass
