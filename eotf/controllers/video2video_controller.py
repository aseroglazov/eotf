from numpy import ndarray

from eotf.use_cases.initialization import get_initialized_domain
from eotf.use_cases.video2video import Video2VideoHandler
from .video_presenter import AbstractVideoOutput, VideoPresenter


class Video2VideoController:
    def __init__(self, output: AbstractVideoOutput):
        self.domain = get_initialized_domain()
        self.presenter = VideoPresenter(output)
        self.video_handler = Video2VideoHandler(self.domain, self.presenter)

    def consume(self, frame: ndarray):
        self.video_handler.consume(frame)
