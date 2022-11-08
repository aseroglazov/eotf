import logging

from eotf.figures import Text
from eotf.helpers import \
    get_angle, \
    Point3D


FINGER_OFFSET = {
    'THUMB': 1,
    'INDEX_FINGER': 5,
    'MIDDLE_FINGER': 9,
    'RING_FINGER': 13,
    'PINKY': 17
}


logger = logging.getLogger(name=__name__)
logger.propagate = True


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
        return self.pip_angle < 110


class HandStructure:
    def __init__(self, landmarks: tuple[Point3D]):
        def finger_landmarks(finger_name: str):
            result = []
            initial_offset = FINGER_OFFSET[finger_name.upper()]
            for index in range(initial_offset, initial_offset + 4):
                result.append(landmarks[index])

            return result

        self.wrist = landmarks[0]

        self.thumb = Finger(finger_landmarks('THUMB'))
        self.index_finger = Finger(finger_landmarks('INDEX_FINGER'))
        self.middle_finger = Finger(finger_landmarks('MIDDLE_FINGER'))
        self.ring_finger = Finger(finger_landmarks('RING_FINGER'))
        self.pinky = Finger(finger_landmarks('PINKY'))

        logger.debug(
            f'index pip angle is %s',
            Text(
                bottom_left_corner_of_text=self.index_finger.PIP,
                message=f'{int(self.index_finger.pip_angle)}'
            )
        )

    def knuckles_are_horizontal(self) -> bool:
        imaginary_point_for_horizon = Point3D(
                                                x=self.pinky.MCP.x,
                                                y=self.index_finger.MCP.y,
                                                z=self.pinky.MCP.z
                                            )
        angle = get_angle(imaginary_point_for_horizon, self.index_finger.MCP, self.pinky.MCP)
        logger.debug(
            f'index horizon angle is %s',
            Text(
                bottom_left_corner_of_text=self.index_finger.MCP,
                message=f'{int(angle)}'
            )
        )
        return angle < 45
