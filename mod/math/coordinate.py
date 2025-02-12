from __future__ import annotations

from .vector2 import Vector2
from typing import override


class Coordinate(Vector2):
    def __init__(self, x: int = 0, y: int = 0) -> None:
        super().__init__(x, y)

    def __repr__(self) -> str:
        return f"Coordinate(x='{self.x}', y='{self.y}')"

    def get_x(self) -> float:
        return self.x

    def get_y(self) -> float:
        return self.y

    def increament_x(self, a: float = 1):
        self.x += a

    def increament_y(self, a: float = 1):
        self.y += a

    def decrement_x(self, a: float = 1):
        self.x -= a

    def decrement_y(self, a: float = 1):
        self.y -= a

    @override
    @classmethod
    def rand(cls, limit_x: Vector2, limit_y: Vector2) -> Coordinate:
        from random import randint

        x: int = randint(int(limit_x.x), int(limit_x.y))
        y: int = randint(int(limit_y.x), int(limit_y.y))
        return cls(x, y)
