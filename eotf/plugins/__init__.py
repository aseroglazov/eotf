from .base import BasePlugin
from .finger_drawing import FingerDrawingPlugin
from .hand_detection import HandDetectionPlugin
from .virtual_camera import VirtualCameraPlugin
from .landmark_visualizer import LandmarkVisualizerPlugin
from .summary_visualizer import SummaryVisualizerPlugin


class PluginChain:
    def __init__(self, send_to_virtual_camera=True, show_landmarks=True, show_result=True):
        self.active_plugins = []
        self.setup_plugins(send_to_virtual_camera, show_landmarks, show_result)

    def setup_plugins(self, send_to_virtual_camera, show_landmarks, show_result):
        self.active_plugins = [
            HandDetectionPlugin()
        ]

        if show_landmarks:
            self.active_plugins.append(LandmarkVisualizerPlugin())

        self.active_plugins.append(FingerDrawingPlugin())

        if show_result:
            self.active_plugins.append(SummaryVisualizerPlugin())
        if send_to_virtual_camera:
            self.active_plugins.append(VirtualCameraPlugin())

    def __call__(self):
        pass

    def deal_with(self, scene):
        for plugin in self.active_plugins:
            scene = plugin.deal_with(scene)
        return scene

    def close(self):
        for plugin in self.active_plugins:
            plugin.close()
