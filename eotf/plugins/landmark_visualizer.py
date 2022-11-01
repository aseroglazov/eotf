import mediapipe as mp
from mediapipe.framework.formats.landmark_pb2 import NormalizedLandmarkList
from numpy import ndarray

from .base import BasePlugin
from eotf.hand import Hand
from eotf.helpers import Scene


class LandmarkVisualizerPlugin(BasePlugin):
    @staticmethod
    def _visualize_hand_landmarks(image: ndarray, landmarks: NormalizedLandmarkList) -> None:
        mp.solutions.drawing_utils.draw_landmarks(
            image,
            landmarks,
            mp.solutions.hands.HAND_CONNECTIONS,
            mp.solutions.drawing_styles.get_default_hand_landmarks_style(),
            mp.solutions.drawing_styles.get_default_hand_connections_style())

    def deal_with(self, scene: Scene) -> Scene:
        for item in scene.detected_objects:
            if isinstance(item, Hand):
                self._visualize_hand_landmarks(scene.image, item.raw_landmarks)
        return scene
