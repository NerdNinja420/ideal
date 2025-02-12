from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..math.coordinate import Coordinate

from .object import Object, ObjectType


class Skatt(Object):
    def __init__(self, coordinates: Coordinate, value: int, ID: str = "S") -> None:
        super().__init__(coordinates, ID, ObjectType.SKATT)
        self.value = value

    @classmethod
    def from_base_class(cls, base: Object) -> Skatt:
        att = base.__getattribute__("value")
        if att:
            return cls(base.coordinates, att, base.ID)
        raise AttributeError(f"{base} does not have attribute 'value'")
