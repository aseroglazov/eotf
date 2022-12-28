import cv2
from numpy import ndarray


class VideoCameraSource:
    def __init__(self, camera_id: int, image_width: int, image_height: int, mirror: bool = True):
        self.video = cv2.VideoCapture(camera_id)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, image_width)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, image_height)
        self.mirror = mirror

    def __iter__(self) -> ndarray:
        while self.video.isOpened():
            success, image = self.video.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue
            if self.mirror:
                image = cv2.flip(image, 1)
            yield image
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.close()

    def close(self) -> None:
        self.video.release()
