from .drone import Drone
from .charger import Charger
from ..math.coordinate import Coordinate


class Base(Charger):
    def __init__(
        self, drones: list[Drone], coordinates: Coordinate = Coordinate(), ID: str = "B"
    ) -> None:
        super().__init__(coordinates, ID)
        self.drones = drones

    def __str__(self) -> str:
        return f"Base(coordinates='{self.coordinates}', drones='{self.drones}', ID='{self.ID}')"

    def get_drones(self) -> list[Drone]:
        return self.drones
