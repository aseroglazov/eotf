import cv2
import mediapipe as mp
from numpy import ndarray

from .base import BasePlugin
from eotf.gesture import DetectedHand
from eotf.scene import Scene


class HandDetectionPlugin(BasePlugin):
    def __init__(self):
        self.detector = mp.solutions.hands.Hands(
            model_complexity=0,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def _detect_hands(self, image: ndarray) -> list[DetectedHand]:
        detected_hands = []

        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        rgb_image.flags.writeable = False

        found_hands = self.detector.process(rgb_image)
        if found_hands.multi_handedness:
            for index, hand in enumerate(found_hands.multi_handedness):
                detected_hands.append(
                    DetectedHand(
                        side=hand.classification[0].label.lower(),
                        landmarks=found_hands.multi_hand_landmarks[index]
                    )
                )
        return detected_hands

    def deal_with(self, scene: Scene) -> Scene:
        scene.detected_objects = self._detect_hands(scene.image)

        return scene

    def close(self) -> None:
        self.detector.close()
