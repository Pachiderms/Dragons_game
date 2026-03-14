import pygame
from game import Game
import math
from pygame import mouse
import time
import os
pygame.init()


Fps = 120
clock = pygame.time.Clock()

save_dir = "logs/"

pygame.display.set_caption("Dragons Fly")
screen = pygame.display.set_mode((1080, 600))


background = pygame.image.load("assets_dragons/beurk.jpg")

banner = pygame.image.load("assets_dragons/toothless_head.jpg")

fight_button = pygame.image.load("assets_dragons/hey.jpg")
fight_button_rect = fight_button.get_rect()
fight_button_rect.x = math.ceil(screen.get_width() / 2.9)
fight_button_rect.y = math.ceil(screen.get_height() / 1.4)
highest_score = 0

game = Game()

running = True


def quit_game():
    # r=read, a=append, w=write, x=create; handle as t=text, b=binary
    if os.path.isfile(save_dir + "var_logs.txt"):
        file = open(save_dir + "var_logs.txt", "a")
    else:
        file = open(save_dir + "var_logs.txt", "x")

    if not game.best_score == 0:
        file.write(str(game.best_score) + "\n")

    file.close()

def high_score():
    hs = 0
    tmp = "0"
    if os.path.isfile(save_dir + "var_logs.txt") and game.best_score == 0:
        file = open(save_dir + "var_logs.txt", "r")
        tmp = file.readline()
        while tmp:
            score = tmp[:-len("\n")]
            if not score:
                break
            if float(score) > hs:
                hs = float(score)
            tmp = file.readline()
        file.close()
    else:
        hs = game.best_score

    highest_score_text = font.render(f"Highest Score : {hs}", False, (22, 229, 86))
    screen.blit(highest_score_text, (0, 0))

while running:

    screen.blit(background, (0, 0))
    pygame.mouse.set_cursor(pygame.cursors.diamond)

    if game.is_playing:
        game.update(screen)
        if highest_score <= game.score:
            highest_score = game.score

    else:
        screen.blit(banner, (0, 0))
        screen.blit(fight_button, fight_button_rect)

        font = pygame.font.SysFont("monospace", 15)
        high_score()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit_game()
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_ESCAPE:
                running = False
                quit_game()
                pygame.quit()
            elif event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.lose_stamina_fire_ball()
                else:
                    game.start()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if fight_button_rect.collidepoint(event.pos):
                game.start()
