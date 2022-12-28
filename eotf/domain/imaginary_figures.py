from abc import abstractmethod

from .tools import Point3D


class ImaginaryFigure:
    def __init__(self, start_point: Point3D, end_point: Point3D):
        self.start_point = start_point
        self.end_point = end_point


class ImaginaryLine(ImaginaryFigure):
    pass


class ImaginaryRectangle(ImaginaryFigure):
    pass


class AbstractFilterOfImaginaryFigures:
    @abstractmethod
    def __call__(self, item: ImaginaryFigure) -> bool:
        raise NotImplementedError


class ActiveImaginaryFigures:
    def __init__(self):
        self._storage = []
        self._index = 0

    def __iter__(self):
        for i in range(len(self)):
            yield self._storage[i]

    def __len__(self):
        return len(self._storage)

    def __index__(self):
        try:
            element = self[self._index]
        except IndexError:
            raise StopIteration()
        self._index += 1
        return element

    def __getitem__(self, index: int):
        return self._storage[index]

    def __contains__(self, item: ImaginaryFigure):
        for i in self:
            if i == item:
                return True
        return False

    def add(self, item: ImaginaryFigure):
        self._storage.append(item)

    def filter_by(self, filtering_conditions: AbstractFilterOfImaginaryFigures) -> list[ImaginaryFigure]:
        result = []
        for item in self:
            if not filtering_conditions(item):
                continue
            result.append(item)
        return result

    def remove(self, item):
        self._storage.remove(item)
