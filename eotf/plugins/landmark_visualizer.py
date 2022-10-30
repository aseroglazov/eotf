import mediapipe as mp

from .base import BasePlugin
from eotf.hand import Hand


class LandmarkVisualizerPlugin(BasePlugin):
    @staticmethod
    def _visualize_hand_landmarks(image, landmarks):
        mp.solutions.drawing_utils.draw_landmarks(
            image,
            landmarks,
            mp.solutions.hands.HAND_CONNECTIONS,
            mp.solutions.drawing_styles.get_default_hand_landmarks_style(),
            mp.solutions.drawing_styles.get_default_hand_connections_style())

    def deal_with(self, scene):
        for item in scene.detected_objects:
            if isinstance(item, Hand):
                self._visualize_hand_landmarks(scene.image, item.landmarks)
        return scene
