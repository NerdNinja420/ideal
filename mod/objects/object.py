from enum import Enum, auto

from .map import Map
from ..math.coordinate import Coordinate


class ObjectType(Enum):
    DRONE = auto()
    SKATT = auto()
    CHARGER = auto()


class Object:
    def __init__(
        self, coordinates: Coordinate, ID: str, objectType: ObjectType, map: Map | None = None
    ) -> None:
        self.coordinates = coordinates
        self.ID = ID
        self.objectType = objectType
        self.map = map

    def __repr__(self) -> str:
        return f"Object(coordinates='{self.coordinates}', ID='{self.ID}', objectType='{self.objectType}', map='{self.map}')"

    def get_coordinates(self) -> Coordinate:
        return self.coordinates

    def get_ID(self) -> str:
        return self.ID

    def get_objectType(self) -> ObjectType:
        return self.objectType
