from abc import ABC, abstractmethod

from eotf.helpers import Scene


class AbstractPlugin(ABC):
    @abstractmethod
    def deal_with(self, scene: Scene) -> Scene:
        raise NotImplementedError

    @abstractmethod
    def close(self) -> None:
        raise NotImplementedError


class BasePlugin(AbstractPlugin):
    def deal_with(self, scene: Scene) -> Scene:
        return scene

    def close(self) -> None:
        pass
