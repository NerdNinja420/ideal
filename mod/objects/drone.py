from .skatt import Skatt
from ..math.coordinate import Coordinate
from ..math.direction import Direction
from .object import Object, ObjectType
from ..math.constants import POWER_CUNSUMPTION, MAX_POWER, MAX_SKATT


class Drone(Object):
    def __init__(
        self, coordinates: Coordinate, power: int, ID: str = "D", skatt: int | None = None
    ) -> None:
        super().__init__(coordinates, ID, ObjectType.DRONE)
        self.power = power
        self.skatt_collected = skatt if skatt else 0

    def __repr__(self) -> str:
        return (
            f"Drone(coorinates='{self.coordinates}',"
            f" power='{self.power}',"
            f" skatt='{self.skatt_collected}')"
        )

    def collect(self) -> bool:
        if self.map:
            if (nearest_s := 
                    self.map.get_nearest(self, ObjectType.SKATT)).coordinates == self.coordinates:  # fmt:skip
                if (s := Skatt.from_base_class(nearest_s)).value + self.skatt_collected <= MAX_SKATT:  # fmt:skip
                    self.skatt_collected += s.value

        raise NameError(f"Object:{self}, has no map!")

    def move(self, direction: Direction) -> bool:
        if self.map:
            nearest_charger = self.map.get_nearest(self, ObjectType.CHARGER)
            distance_to_nearest_charger = self.map.get_distance(self, nearest_charger)

            if distance_to_nearest_charger * POWER_CUNSUMPTION > self.power - 1:
                print("before match")
                match direction:
                    case Direction.RIGHT:
                        self.coordinates.increament_x()
                    case Direction.LEFT:
                        self.coordinates.decrement_x()
                    case Direction.UP:
                        self.coordinates.increament_y()
                    case Direction.DOWN:
                        self.coordinates.decrement_y()
                    case Direction.NONE:
                        return False
                return True

            print(f"not enouph power{nearest_charger}")
            return False
        raise NameError(f"Object:{self}, has no map!")

    def charge(self) -> Coordinate:
        if self.map:
            self.coordinates = self.map.get_nearest(self, ObjectType.CHARGER).coordinates
            self.power = MAX_POWER
            return self.coordinates
        raise NameError(f"Object:{self}, has no map!")
