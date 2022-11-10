from eotf.helpers import \
    get_angle, \
    Point3D


class FingerException(Exception):
    pass


class Finger:
    def __init__(self, landmarks: list[Point3D]):
        try:
            self.MCP, self.PIP, self.DIP, self.TIP = landmarks
        except ValueError:
            raise FingerException(f'Wrong format of landmarks. Must be 4 points, got {len(landmarks)}')

    @property
    def pip_angle(self):
        return get_angle(self.DIP, self.PIP, self.MCP)

    def is_straight(self) -> bool:
        return self.pip_angle > 160

    def is_crunched(self) -> bool:
        #TODO: Deal with situation when fingers are crunched, but looks directly to camera. Angle is calculated wrong
        return self.pip_angle < 110
