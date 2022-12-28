from eotf.domain.tools import get_inheritors
from .basic import BasicMotion
from .draw_line import DrawLineMotion
from .erasing import ErasingMotion
from .rectangle import DrawRectangleMotion, \
    DragMotion
from .filtering import FilteringConditions


def get_all_known_motions():
    return get_inheritors(BasicMotion)

__all__ = [
    'get_all_known_motions',
    'BasicMotion',
    'DrawLineMotion',
    'DragMotion', 'DrawRectangleMotion',
    'ErasingMotion',
    'FilteringConditions'
]
