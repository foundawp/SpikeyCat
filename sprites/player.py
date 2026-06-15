import pygame
from settings import ORANGE

class Player:

    def __init__(self):

        self.width = 60
        self.height = 60

        self.x = 120
        self.y = 350

        self.ground_y = 350

        self.velocity_y = 0

        self.gravity = 1
        self.jump_strength = -18

        self.animation_timer = 0

    def jump(self):

        if self.y >= self.ground_y:
            self.velocity_y = self.jump_strength

    def update(self):

        self.velocity_y += self.gravity
        self.y += self.velocity_y

        if self.y > self.ground_y:
            self.y = self.ground_y
            self.velocity_y = 0

        self.animation_timer += 1

    @property
    def rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )

    def draw(self, screen):

        body = pygame.Rect(
            self.x,
            self.y + 15,
            self.width,
            self.height - 15
        )

        pygame.draw.rect(screen, ORANGE, body)

        head = pygame.Rect(
            self.x + 35,
            self.y,
            25,
            25
        )

        pygame.draw.rect(screen, ORANGE, head)

        pygame.draw.polygon(
            screen,
            ORANGE,
            [
                (self.x + 38, self.y),
                (self.x + 43, self.y - 10),
                (self.x + 48, self.y)
            ]
        )

        pygame.draw.polygon(
            screen,
            ORANGE,
            [
                (self.x + 52, self.y),
                (self.x + 57, self.y - 10),
                (self.x + 62, self.y)
            ]
        )

        if self.y >= self.ground_y:

            offset = 3 if (self.animation_timer // 6) % 2 else -3

            pygame.draw.line(
                screen,
                (0,0,0),
                (self.x + 15, self.y + 55),
                (self.x + 15, self.y + 55 + offset),
                3
            )

            pygame.draw.line(
                screen,
                (0,0,0),
                (self.x + 40, self.y + 55),
                (self.x + 40, self.y + 55 - offset),
                3
            )