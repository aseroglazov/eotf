import pyvirtualcam

from .base import BasePlugin
from ..settings import IMAGE_WIDTH, IMAGE_HEIGHT, VIDEO_FPS


class VirtualCameraPlugin(BasePlugin):
    def __init__(self):
        self.virtual_camera = pyvirtualcam.Camera(
            width=IMAGE_WIDTH,
            height=IMAGE_HEIGHT,
            fps=VIDEO_FPS,
            fmt=pyvirtualcam.PixelFormat.BGR
        )
        print(f'Using virtual camera: {self.virtual_camera.device}')

    def deal_with(self, scene):
        self.virtual_camera.send(scene.image)
        self.virtual_camera.sleep_until_next_frame()
        return scene

    def close(self):
        self.virtual_camera.close()
