import pygame

pygame.init()

info = pygame.display.Info()

WIDTH = info.current_w
HEIGHT = info.current_h

FPS = 60

GROUND_Y = HEIGHT - 90

WHITE = (245, 245, 245)
BLACK = (20, 20, 20)
GRAY = (180, 180, 180)
ORANGE = (255, 170, 40)
GREEN = (50, 180, 50)

pygame.font.init()

TITLE_FONT = pygame.font.SysFont(
    "consolas",
    64,
    bold=True
)

MENU_FONT = pygame.font.SysFont(
    "consolas",
    32
)

SMALL_FONT = pygame.font.SysFont(
    "consolas",
    22
)

HIGHSCORE_FILE = "highscore.txt"