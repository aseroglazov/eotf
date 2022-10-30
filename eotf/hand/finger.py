from ..helpers import distance


class FingerException(Exception):
    pass


class Finger:
    def __init__(self, landmarks):
        try:
            self.MCP, self.PIP, self.DIP, self.TIP = landmarks
        except ValueError:
            raise FingerException(f'Wrong format of landmarks. Must be 4 points, got {len(landmarks)}')

    def is_straight(self):
        return distance(self.TIP, self.MCP) \
               > \
               distance(self.MCP, self.PIP) + distance(self.PIP, self.DIP)

    def is_crunched(self):
        return distance(self.TIP, self.MCP) \
               < \
               distance(self.MCP, self.PIP) + distance(self.PIP, self.DIP)
