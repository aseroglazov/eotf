import logging

from .finger import Finger
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


class Hand:
    def __init__(self, side: str, landmarks: tuple[Point3D]):
        def finger_landmarks(finger_name: str):
            return self._get_finger_landmarks(finger_name, landmarks)

        self.side = side

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

    def _get_finger_landmarks(self, finger_name: str, landmarks: tuple[Point3D]):
            result = []
            initial_offset = FINGER_OFFSET[finger_name.upper()]
            for index in range(initial_offset, initial_offset + 4):
                result.append(landmarks[index])
            return result

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
