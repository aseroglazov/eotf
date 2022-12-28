from .videocamera import VideoCameraSource
from .window import WindowVideoOutput
from .settings import DEFAULT_CAMERA_ID, DEFAULT_IMAGE_WIDTH, DEFAULT_IMAGE_HEIGHT
from eotf.controllers import Video2VideoController


DEFAULT_INPUT = VideoCameraSource(
    camera_id=DEFAULT_CAMERA_ID,
    image_width=DEFAULT_IMAGE_WIDTH,
    image_height=DEFAULT_IMAGE_HEIGHT
)
DEFAULT_OUTPUT = WindowVideoOutput()


def start_drawing(input=DEFAULT_INPUT, output=DEFAULT_OUTPUT, controller=None):
    if controller is None:
        controller = Video2VideoController(output)
    for frame in input:
        controller.consume(frame)
