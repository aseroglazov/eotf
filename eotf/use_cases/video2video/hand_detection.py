import cv2
import mediapipe as mp
from numpy import ndarray
from mediapipe.framework.formats.landmark_pb2 import NormalizedLandmarkList

from eotf.domain import Point3D, AbstractHand
from .settings import MODEL_COMPLEXITY, \
    MIN_DETECTION_CONFIDENCE, \
    MIN_TRACKING_CONFIDENCE


def convert_to_point3d(landmarks: mp.framework.formats.landmark_pb2.NormalizedLandmarkList) -> list[Point3D]:
    result = []
    for landmark in landmarks.landmark:
        result.append(Point3D(landmark.x, landmark.y, landmark.z))
    return result


class HandDetection:
    def __init__(self, hand_cls: AbstractHand):
        self.hand_cls = hand_cls

        self.detector = mp.solutions.hands.Hands(
            model_complexity=MODEL_COMPLEXITY,
            min_detection_confidence=MIN_DETECTION_CONFIDENCE,
            min_tracking_confidence=MIN_TRACKING_CONFIDENCE
        )

    def get_hands(self, image: ndarray) -> list[AbstractHand]:
        detected_hands = []

        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        rgb_image.flags.writeable = False

        found_hands = self.detector.process(rgb_image)
        if found_hands.multi_handedness:
            for index, hand in enumerate(found_hands.multi_handedness):
                detected_hands.append(
                    self.hand_cls(
                        side=hand.classification[0].label.lower(),
                        landmarks=convert_to_point3d(found_hands.multi_hand_landmarks[index])
                    )
                )
        return detected_hands

    def close(self) -> None:
        self.detector.close()
