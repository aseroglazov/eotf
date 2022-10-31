from mediapipe.python.solutions.hands import HandLandmark

from eotf.helpers import distance


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
