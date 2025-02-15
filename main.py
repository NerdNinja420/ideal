from os import environ
from platform import system

import pygame
from pygame.locals import QUIT

from mod.math.constants import FPS, WIN_WIDTH, WIN_HEIGHT
from mod.color import Color

if system() == "Linux":
    environ["SDL_VIDEO_WINDOW_POS"] = "{},{}".format(-1650, 100)


def main():
    pygame.init()
    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    CLOCK = pygame.time.Clock()

    WIN.fill(Color.BASE.rgb())

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        for row in range(int(WIN_HEIGHT / 11)):
            width: int = int((WIN_HEIGHT - 11) / 10)

            print(
                f"Drawing horizontal line at y={(width * row + 1 * row + (1 * row))}"
            )  # Debugging
            pygame.draw.line(
                WIN,
                Color.RED.rgb(),
                (0, width * row + 1 * row + (1 * row)),
                (WIN_WIDTH, width * row + 1 * row + (1 * row)),
            )
        for col in range(int(WIN_WIDTH / 11)):
            width: int = int((WIN_HEIGHT - 11) / 10)

            print(
                f"Drawing horizontal line at y={(width * col + 1 * col + (1 * col))}"
            )  # Debugging
            pygame.draw.line(
                WIN,
                Color.RED.rgb(),
                (width * col + 1 * col + (1 * col), 0),
                (width * col + 1 * col + (1 * col), WIN_HEIGHT),
            )

        pygame.display.update()

        CLOCK.tick(FPS)


if __name__ == "__main__":
    main()
