import cv2

from eotf.settings import IMAGE_HEIGHT, \
    IMAGE_WIDTH


class VideoSource:
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, IMAGE_WIDTH)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, IMAGE_HEIGHT)

    def __iter__(self):
        while self.video.isOpened():
            success, image = self.video.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue
            yield image
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.close()

    def close(self):
        self.video.release()
