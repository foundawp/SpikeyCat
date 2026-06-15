import pygame
import random

class Cloud:

    def __init__(self):

        self.x = random.randint(0, 1200)
        self.y = random.randint(50, 180)

        self.speed = random.uniform(1, 2)

    def update(self):

        self.x -= self.speed

        if self.x < -100:
            self.x = 1300

    def draw(self, screen):

        pygame.draw.circle(
            screen,
            (180,180,180),
            (int(self.x), self.y),
            20,
            2
        )

        pygame.draw.circle(
            screen,
            (180,180,180),
            (int(self.x)+20, self.y-10),
            20,
            2
        )

        pygame.draw.circle(
            screen,
            (180,180,180),
            (int(self.x)+40, self.y),
            20,
            2
        )