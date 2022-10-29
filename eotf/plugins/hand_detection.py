import cv2
import mediapipe as mp

from .base import BasePlugin
from ..hand import Hand


class HandDetectionPlugin(BasePlugin):
    def __init__(self):
        self.detector = mp.solutions.hands.Hands(
            model_complexity=0,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def _detect_hands(self, image):
        detected_hands = []

        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        rgb_image.flags.writeable = False

        found_hands = self.detector.process(rgb_image)
        if found_hands.multi_handedness:
            for index, hand in enumerate(found_hands.multi_handedness):
                detected_hands.append(
                    Hand(
                        side=hand.classification[0].label.lower(),
                        landmarks=found_hands.multi_hand_landmarks[index]
                    )
                )
        return detected_hands

    def deal_with(self, scene):
        scene.detected_objects = self._detect_hands(scene.image)

        return scene

    def close(self):
        self.detector.close()
