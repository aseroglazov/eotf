import cv2

from eotf import \
    VideoSource, \
    PluginChain, \
    Scene


def main(send_to_virtual_camera: bool, visualize_hands: bool):
    plugins = PluginChain(send_to_virtual_camera=send_to_virtual_camera, show_landmarks=visualize_hands)
    video = VideoSource()
    for frame in video:
        scene = Scene(cv2.flip(frame, 1))
        plugins.deal_with(scene)
    plugins.close()


if __name__ == '__main__':
    main(send_to_virtual_camera=False, visualize_hands=True)
