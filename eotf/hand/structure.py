from mediapipe.python.solutions.hands import HandLandmark
from mediapipe.framework.formats.landmark_pb2 import NormalizedLandmarkList

from eotf.helpers import distance


FINGER_OFFSET = {
    'THUMB': 1,
    'INDEX_FINGER': 5,
    'MIDDLE_FINGER': 9,
    'RING_FINGER': 13,
    'PINKY': 17
}


class FingerException(Exception):
    pass


class Finger:
    def __init__(self, landmarks: list[HandLandmark]):
        try:
            self.MCP, self.PIP, self.DIP, self.TIP = landmarks
        except ValueError:
            raise FingerException(f'Wrong format of landmarks. Must be 4 points, got {len(landmarks)}')

    def is_straight(self) -> bool:
        return distance(self.TIP, self.MCP) \
               > \
               distance(self.MCP, self.PIP) + distance(self.PIP, self.DIP)

    def is_crunched(self) -> bool:
        return distance(self.TIP, self.MCP) \
               < \
               distance(self.MCP, self.PIP) + distance(self.PIP, self.DIP)


class HandStructure:
    def __init__(self, landmarks: NormalizedLandmarkList):
        def finger_landmarks(finger_name: str):
            result = []
            initial_offset = FINGER_OFFSET[finger_name.upper()]
            for index in range(initial_offset, initial_offset + 4):
                result.append(landmarks.landmark[index])

            return result

        self.wrist = landmarks.landmark[0]

        self.thumb = Finger(finger_landmarks('THUMB'))
        self.index_finger = Finger(finger_landmarks('INDEX_FINGER'))
        self.middle_finger = Finger(finger_landmarks('MIDDLE_FINGER'))
        self.ring_finger = Finger(finger_landmarks('RING_FINGER'))
        self.pinky = Finger(finger_landmarks('PINKY'))
