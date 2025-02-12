from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .object import Object, ObjectType

from ..math.constants import MAX_MIN_X, MAX_MIN_Y


class Map(Object):
    def __init__(
        self,
        objects: list[Object],
        borders_x: list[float] = MAX_MIN_X,
        borders_y: list[float] = MAX_MIN_Y,
    ) -> None:
        self.objects = objects
        self.borders_x = borders_x
        self.borders_y = borders_y
        for obj in self.objects:
            obj.map = self

    def __repr__(self) -> str:
        return (
            f"Map(Objects='{len(self.objects)}',"
            f" borders_x='{self.borders_x}',"
            f" borders_y='{self.borders_y}')"
        )

    def is_insight(self, obj: Object) -> bool:
        return (
            obj.get_coordinates().get_x() <= self.borders_x[1]
            and obj.get_coordinates().get_y() <= self.borders_y[1]
        )

    def get_distance(self, obj_1: Object, obj_2: Object) -> float:
        from math import sqrt

        return sqrt(
            ((obj_2.coordinates.get_x() - obj_1.coordinates.get_x()) ** 2)
            + ((obj_2.coordinates.get_y() - obj_1.coordinates.get_y()) ** 2)
        )

    def get_nearest(self, obj: Object, obj_2_Type: ObjectType) -> Object:
        from math import sqrt

        ob: Object = obj
        d: float = sqrt((MAX_MIN_X[1] * 2) ** 2 + (MAX_MIN_Y[1] * 2) ** 2)  # pytagoras for diagonal

        obj_with_same_objectType = [o for o in self.objects if o.get_objectType() == obj_2_Type]
        if len(obj_with_same_objectType) > 0:
            for object in obj_with_same_objectType:
                if self.is_insight(object) and self.get_distance(obj, object) < d:
                    d = self.get_distance(obj, object)
                    ob = object
                    print(f"{ob} at getnearest")
            return ob
        raise NameError(f"{self} has no charger!")

    @classmethod
    def get_distance_cls(cls, obj_1: Object, obj_2: Object) -> float:
        from math import sqrt

        return sqrt(
            ((obj_2.coordinates.get_x() - obj_1.coordinates.get_x()) ** 2)
            + ((obj_2.coordinates.get_y() - obj_1.coordinates.get_y()) ** 2)
        )
