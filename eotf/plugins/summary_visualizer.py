import cv2

from .base import BasePlugin
from eotf.helpers import Scene


class SummaryVisualizerPlugin(BasePlugin):
    def deal_with(self, scene: Scene) -> Scene:
        cv2.imshow('Explain on the fingers', scene.image)
        return scene
