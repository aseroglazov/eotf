from .base import BasePlugin
from .finger_drawing import FingerDrawingPlugin
from .hand_detection import HandDetectionPlugin
from .virtual_camera import VirtualCameraPlugin
from .landmark_visualizer import LandmarkVisualizerPlugin
from .summary_visualizer import SummaryVisualizerPlugin
from eotf.helpers import Scene


class PluginChain:
    def __init__(self, send_to_virtual_camera: bool = True, show_landmarks: bool = True, show_result: bool = True):
        self.active_plugins = []
        self._setup_plugins(send_to_virtual_camera, show_landmarks, show_result)

    def _setup_plugins(self, send_to_virtual_camera: bool, show_landmarks: bool, show_result: bool):
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

    def deal_with(self, scene: Scene) -> Scene:
        for plugin in self.active_plugins:
            scene = plugin.deal_with(scene)
        return scene

    def close(self) -> None:
        for plugin in self.active_plugins:
            plugin.close()
