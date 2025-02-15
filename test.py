import pygame
from pygame.locals import QUIT

from mod.math.constants import FPS, WIN_WIDTH, WIN_HEIGHT
from mod.color import Color


def main():
    pygame.init()
    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    CLOCK = pygame.time.Clock()
    WIN.fill(Color.BASE.rgb())

    # Grid parameters
    rows = 10
    cols = 10
    row_height = WIN_HEIGHT // rows
    col_width = WIN_WIDTH // cols

    # Debugging print
    print(f"Grid details: row_height={row_height}, col_width={col_width}")

    # Draw horizontal lines
    for row in range(rows + 1):  # Ensure last line is included
        y = row * row_height
        print(f"Drawing horizontal line at y={y}")  # Debugging
        pygame.draw.line(WIN, Color.RED.rgb(), (0, y), (WIN_WIDTH, y))

    # Draw vertical lines
    for col in range(cols + 1):  # Ensure last line is included
        x = col * col_width
        print(f"Drawing vertical line at x={x}")  # Debugging
        pygame.draw.line(WIN, Color.RED.rgb(), (x, 0), (x, WIN_HEIGHT))

    pygame.display.update()

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        CLOCK.tick(FPS)


if __name__ == "__main__":
    main()
