import pygame
import random

from settings import *
from sprites.player import Player
from sprites.obstacle import Obstacle
from sprites.cloud import Cloud

class Game:

    def __init__(self):

        self.reset()

    def reset(self):

        self.player = Player()

        self.score = 0
        self.speed = 8

        self.spawn_timer = 0

        self.obstacles = []

        self.clouds = [
            Cloud()
            for _ in range(5)
        ]

        self.game_over = False

    def update(self):

        if self.game_over:
            return

        self.score += 1

        self.speed += 0.001

        self.player.update()

        for cloud in self.clouds:
            cloud.update()

        self.spawn_timer += 1

        if self.spawn_timer > random.randint(60,120):

            self.obstacles.append(
                Obstacle(self.speed)
            )

            self.spawn_timer = 0

        for obstacle in self.obstacles[:]:

            obstacle.speed = self.speed
            obstacle.update()

            if obstacle.x < -100:
                self.obstacles.remove(obstacle)

            if self.player.rect.colliderect(
                obstacle.rect
            ):
                self.game_over = True

    def draw(self, screen, highscore):

        screen.fill(WHITE)

        pygame.draw.line(
            screen,
            BLACK,
            (0,GROUND_Y),
            (WIDTH,GROUND_Y),
            3
        )

        for cloud in self.clouds:
            cloud.draw(screen)

        self.player.draw(screen)

        for obstacle in self.obstacles:
            obstacle.draw(screen)

        screen.blit(
            MENU_FONT.render(
                f"Score: {self.score}",
                True,
                BLACK
            ),
            (20,20)
        )

        screen.blit(
            MENU_FONT.render(
                f"High Score: {highscore}",
                True,
                BLACK
            ),
            (20,60)
        )

        if self.game_over:

            overlay = pygame.Surface(
                (WIDTH,HEIGHT)
            )

            overlay.set_alpha(180)
            overlay.fill(WHITE)

            screen.blit(overlay,(0,0))

            txt = TITLE_FONT.render(
                "GAME OVER",
                True,
                BLACK
            )

            screen.blit(
                txt,
                (
                    WIDTH//2 - txt.get_width()//2,
                    150
                )
            )

            restart = MENU_FONT.render(
                "R = Restart",
                True,
                BLACK
            )

            menu = MENU_FONT.render(
                "ESC = Menu",
                True,
                BLACK
            )

            screen.blit(
                restart,
                (
                    WIDTH//2 - restart.get_width()//2,
                    250
                )
            )

            screen.blit(
                menu,
                (
                    WIDTH//2 - menu.get_width()//2,
                    300
                )
            )