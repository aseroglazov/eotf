from .base import BasePlugin
from eotf.scene import Scene
from eotf.figures import Figure


class DebugVisualizerPlugin(BasePlugin):
    figures_to_draw = []

    @classmethod
    def add(cls, figure: Figure) -> None:
        cls.figures_to_draw.append(figure)

    @classmethod
    def deal_with(cls, scene: Scene) -> Scene:
        for item in cls.figures_to_draw:
            item.draw_on(scene.image)
        cls.figures_to_draw = []
        return scene
