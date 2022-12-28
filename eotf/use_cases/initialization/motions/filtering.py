from eotf.domain import ImaginaryFigure, \
    AbstractFilterOfImaginaryFigures
from eotf.domain.tools import Point3D

from .helpers import normalize_start_end_points, \
    rectangles_has_interceptions


class FilteringConditions(AbstractFilterOfImaginaryFigures):
    def __init__(self):
        self._area_for_search = None
        self._instance_of = None

    def area_for_search(self, start_point: Point3D, end_point: Point3D):
        self._area_for_search = normalize_start_end_points(start_point, end_point)
        return self

    def instance_of(self, cls_to_compare: ImaginaryFigure):
        self._instance_of = cls_to_compare
        return self

    def _is_in_area(self, item: ImaginaryFigure):
        if self._area_for_search is None:
            return True
        return rectangles_has_interceptions(self._area_for_search, (item.start_point, item.end_point))

    def _is_instance_of(self, item: ImaginaryFigure):
        if self._instance_of is None:
            return True
        return isinstance(item, self._instance_of)

    def __call__(self, item) -> bool:
        return self._is_in_area(item) and self._is_instance_of(item)
