import pygame

from settings import *

class Menu:

    def __init__(self):

        button_width = 320
        button_height = 65

        center_x = WIDTH // 2 - button_width // 2

        self.buttons = [
            (
                "PLAY",
                pygame.Rect(
                    center_x,
                    HEIGHT // 2 - 120,
                    button_width,
                    button_height
                )
            ),
            (
                "SETTINGS",
                pygame.Rect(
                    center_x,
                    HEIGHT // 2 - 40,
                    button_width,
                    button_height
                )
            ),
            (
                "LEADERBOARD",
                pygame.Rect(
                    center_x,
                    HEIGHT // 2 + 40,
                    button_width,
                    button_height
                )
            ),
            (
                "QUIT",
                pygame.Rect(
                    center_x,
                    HEIGHT // 2 + 120,
                    button_width,
                    button_height
                )
            )
        ]

    def draw(self, screen, highscore):

        screen.fill(WHITE)

        title = TITLE_FONT.render(
            "SPIKEY CAT",
            True,
            BLACK
        )

        screen.blit(
            title,
            (
                WIDTH // 2 - title.get_width() // 2,
                HEIGHT // 6
            )
        )

        hs = MENU_FONT.render(
            f"High Score: {highscore}",
            True,
            BLACK
        )

        screen.blit(hs, (20, 20))

        mouse = pygame.mouse.get_pos()

        for text, rect in self.buttons:

            color = ORANGE

            if rect.collidepoint(mouse):
                color = (255, 200, 80)

            pygame.draw.rect(
                screen,
                color,
                rect,
                border_radius=10
            )

            pygame.draw.rect(
                screen,
                BLACK,
                rect,
                3,
                border_radius=10
            )

            txt = MENU_FONT.render(
                text,
                True,
                BLACK
            )

            screen.blit(
                txt,
                (
                    rect.centerx - txt.get_width() // 2,
                    rect.centery - txt.get_height() // 2
                )
            )

        start_text = SMALL_FONT.render(
            "Press SPACE or click PLAY",
            True,
            BLACK
        )

        screen.blit(
            start_text,
            (
                WIDTH // 2 - start_text.get_width() // 2,
                HEIGHT - 100
            )
        )