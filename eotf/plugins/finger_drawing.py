import cv2
import numpy

from .base import BasePlugin
from eotf.settings import \
    IMAGE_WIDTH, \
    IMAGE_HEIGHT
from eotf.gesture_chains import \
    get_all_chain_types, \
    DetectedHand
from eotf.scene import Scene

ALL_CHAIN_TYPES = get_all_chain_types()


class FingerDrawingPlugin(BasePlugin):
    def __init__(self):
        self._clean_state()

    def _clean_state(self):
        self.figures_on_canvas = []
        self.active_chains = {
            'right': [],
            'left': []
        }

    def deal_with(self, scene: Scene) -> Scene:
        for item in scene.detected_objects:
            if isinstance(item, DetectedHand):
                self._process(item)

        scene.image = self._draw_on(scene.image)

        return scene

    def _process(self, hand) -> None:
        consumed_exclusively = False
        for chain in self.active_chains[hand.side]:
            result = chain.send(hand)
            if result.updated:
                consumed_exclusively = result.consumed_exclusively
                break

        if not consumed_exclusively:
            for chain in ALL_CHAIN_TYPES:
                if not chain.starts_with(hand.gesture):
                    continue
                self.active_chains[hand.side].append(chain(hand))

        completed_chains = []
        for index, chain in enumerate(self.active_chains[hand.side]):
            if chain.is_completed():
                self.active_chains[hand.side].pop(index)
                completed_chains.append(chain)
            if chain.is_broken():
                self.active_chains[hand.side].pop(index)

        for chain in completed_chains:
            self.figures_on_canvas.append(chain.result)

    def _draw_on(self, image: numpy.ndarray) -> numpy.ndarray:
        def get_mask(contour: numpy.ndarray) -> numpy.ndarray:
            contour_grey = cv2.cvtColor(contour, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(contour_grey, 10, 255, cv2.THRESH_BINARY)

            return cv2.bitwise_not(mask)

        def join_images(foreground: numpy.ndarray, background: numpy.ndarray) -> numpy.ndarray:
            masked_background = cv2.bitwise_and(background, background, mask=get_mask(foreground))

            return cv2.add(masked_background, foreground)

        canvas = numpy.zeros((IMAGE_HEIGHT, IMAGE_WIDTH, 3), dtype='uint8')

        for figure in self.figures_on_canvas:
            figure.draw_on(canvas)

        return join_images(canvas, image)

    def close(self) -> None:
        self._clean_state()
