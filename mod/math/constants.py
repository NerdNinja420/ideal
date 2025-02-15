from typing import Final
from platform import system


# from ..math.size import Size
from ..math.vector2 import Vector2
# from ..math.coordinate import Coordinate

FPS: Final[int] = 60
EPS: float = 5

if system() == "Linux":
    GAB: Final[int] = 20
    WIN_WIDTH: Final[int] = 1800
    WIN_HEIGHT: Final[int] = 1000
else:
    GAB: Final[int] = 10  # type: ignore
    WIN_WIDTH: Final[int] = 600  # type: ignore
    WIN_HEIGHT: Final[int] = 600  # type: ignore

RECT_SIZE_WIDTH_LIMITS: Final[Vector2] = Vector2(10, int(WIN_WIDTH / 3))
RECT_SIZE_HEIGHT_LIMITS: Final[Vector2] = Vector2(10, int(WIN_HEIGHT / 3))
RECT_POSITION_X_LIMITS: Final[Vector2] = Vector2(0, WIN_WIDTH - RECT_SIZE_WIDTH_LIMITS.y)
RECT_POSITION_Y_LIMITS: Final[Vector2] = Vector2(0, WIN_HEIGHT - RECT_SIZE_HEIGHT_LIMITS.y)

MAX_MIN_X = [-10.0, 10.0]
MAX_MIN_Y = [-10.0, 10.0]
POWER_CUNSUMPTION = 1
MAX_POWER = 30
MAX_SKATT = 50

if system() == "Linux":
    FONT: Final[str] = "JetBrains Mono Nerd Font"
    FONT_SIZE_SCORE: Final[int] = 38
    FONT_SIZE_END_MSG: Final[int] = 100
else:
    FONT: Final[str] = "JetBrainsMono NF SemiBold"  # type: ignore
    FONT_SIZE_SCORE: Final[int] = 20  # type: ignore
    FONT_SIZE_END_MSG: Final[int] = 60  # type: ignore
