from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .drone import Drone


from ..math.coordinate import Coordinate
from .object import Object, ObjectType


class Charger(Object):
    def __init__(self, coordinates: Coordinate, ID: str = "C") -> None:
        super().__init__(coordinates, ID, ObjectType.CHARGER)

    def __repr__(self) -> str:
        return f"Charger(coordinates='{self.coordinates}', ID='{self.ID}', objectType='{self.objectType}'')"

    def charge(self, drone: Drone):
        drone.power = 30
