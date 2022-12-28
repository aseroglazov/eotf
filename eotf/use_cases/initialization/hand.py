from eotf.domain import AbstractHand
from eotf.domain.tools import \
    Point3D, \
    get_angle

from .settings import FINGER_OFFSET, \
    NUMBER_OF_DOTS_PER_FINGER, \
    MIN_ANGLE_FOR_STRAIGHT_FINGER, \
    MAX_ANGLE_FOR_CRUNCHED_FINGER, \
    MAX_ANGLE_FOR_HORIZONTAL_KNUCKLES


class FingerException(Exception):
    pass


class Finger:
    def __init__(self, landmarks: list[Point3D]):
        try:
            self.MCP, self.PIP, self.DIP, self.TIP = landmarks
        except ValueError:
            raise FingerException(f'Wrong format of landmarks. Must be 4 points, got {len(landmarks)}')

    @property
    def pip_angle(self) -> float:
        return get_angle(self.DIP, self.PIP, self.MCP)

    def is_straight(self) -> bool:
        return self.pip_angle > MIN_ANGLE_FOR_STRAIGHT_FINGER

    def is_crunched(self) -> bool:
        #TODO: Deal with situation when fingers are crunched, but looks directly to camera. Angle is calculated wrong
        return self.pip_angle < MAX_ANGLE_FOR_CRUNCHED_FINGER


def get_finger_landmarks(finger_name: str, landmarks: list[Point3D]):
    result = []
    initial_offset = FINGER_OFFSET[finger_name.upper()]
    for index in range(initial_offset, initial_offset + NUMBER_OF_DOTS_PER_FINGER):
        result.append(landmarks[index])
    return result


class Hand(AbstractHand):
    def __init__(self, side: str, landmarks: list[Point3D]):
        self._side = side

        self.wrist = landmarks[0]

        self.thumb = Finger(get_finger_landmarks('THUMB', landmarks))
        self.index_finger = Finger(get_finger_landmarks('INDEX_FINGER', landmarks))
        self.middle_finger = Finger(get_finger_landmarks('MIDDLE_FINGER', landmarks))
        self.ring_finger = Finger(get_finger_landmarks('RING_FINGER', landmarks))
        self.pinky = Finger(get_finger_landmarks('PINKY', landmarks))

    @property
    def side(self) -> str:
        return self._side

    def knuckles_are_horizontal(self) -> bool:
        imaginary_point_for_horizon = Point3D(
                                                x=self.pinky.MCP.x,
                                                y=self.index_finger.MCP.y,
                                                z=self.pinky.MCP.z
                                            )
        angle = get_angle(imaginary_point_for_horizon, self.index_finger.MCP, self.pinky.MCP)

        return angle < MAX_ANGLE_FOR_HORIZONTAL_KNUCKLES

    def handbreadth_is_down(self) -> bool:
        if self.pinky.MCP.x > self.index_finger.MCP.x:
            return self.side == 'right'
        else:
            return self.side == 'left'
