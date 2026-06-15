import pygame
import random
from settings import GREEN

class Obstacle:

    def __init__(self, speed):

        self.width = random.randint(25, 45)
        self.height = random.randint(40, 90)

        self.x = 1250
        self.y = 410 - self.height

        self.speed = speed

    def update(self):

        self.x -= self.speed

    @property
    def rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            GREEN,
            (
                self.x,
                self.y,
                self.width,
                self.height
            )
        )