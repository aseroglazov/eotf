from eotf.domain import DomainHandler, ActiveImaginaryFigures

from .motions import get_all_known_motions
from .hand import Hand


def get_initialized_domain():
    domain_handler = DomainHandler(ActiveImaginaryFigures())
    domain_handler.hand_implementation = Hand
    for motion in get_all_known_motions():
        domain_handler.add_known_motion(motion)

    return domain_handler


__all__ = ['get_initialized_domain']
