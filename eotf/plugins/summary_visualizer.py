import cv2

from .base import BasePlugin


class SummaryVisualizerPlugin(BasePlugin):
    def deal_with(self, scene):
        cv2.imshow('Explain on the fingers', scene.image)
        return scene
