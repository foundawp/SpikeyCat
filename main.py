import pygame
import os

from settings import *
from scenes.menu import Menu
from scenes.game import Game

pygame.init()

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT),
    pygame.FULLSCREEN
)

pygame.display.set_caption(
    "Spikey Cat"
)

clock = pygame.time.Clock()

MENU = 0
PLAYING = 1

state = MENU

menu = Menu()
game = Game()

def load_highscore():

    if os.path.exists(HIGHSCORE_FILE):

        try:

            with open(
                HIGHSCORE_FILE,
                "r"
            ) as file:

                return int(file.read())

        except:
            return 0

    return 0

def save_highscore(score):

    with open(
        HIGHSCORE_FILE,
        "w"
    ) as file:

        file.write(str(score))

highscore = load_highscore()

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()

        if state == MENU:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    game.reset()
                    state = PLAYING

            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse = pygame.mouse.get_pos()

                for text, rect in menu.buttons:

                    if rect.collidepoint(mouse):

                        if text == "PLAY":

                            game.reset()
                            state = PLAYING

                        elif text == "QUIT":

                            running = False

        elif state == PLAYING:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    if not game.game_over:
                        game.player.jump()

                if event.key == pygame.K_ESCAPE:

                    state = MENU

                if game.game_over:

                    if event.key == pygame.K_r:

                        game.reset()

                    if event.key == pygame.K_ESCAPE:

                        state = MENU

    if state == PLAYING:

        game.update()

        if game.score > highscore:

            highscore = game.score
            save_highscore(highscore)

        game.draw(
            screen,
            highscore
        )

    else:

        menu.draw(
            screen,
            highscore
        )

    pygame.display.flip()

pygame.quit()