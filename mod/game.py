from __future__ import annotations

import pygame
from pygame import Surface

from .math.size import Size
from .math.vector2 import Vector2
from .math.coordinate import Coordinate

from .color import Color


class Game:
    def __init__(self, surface: Surface, row: int, col: int) -> None:
        self.surface = surface

    def set_time(self, delta: float):
        self.time = delta

    def set_bg(self):
        self.surface.fill((*Color.BASE,))

    def restart(self):
        pass

    def pause(self, interval: int):
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < interval * (10**3):
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    exit()

    def draw_status(self):
        pass

    def render(self):
        pygame.display.update()
