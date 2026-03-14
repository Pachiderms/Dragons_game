import pygame

import pygame
import random


class BewilderbeastAlly(pygame.sprite.Sprite):
    def __init__(self, fish_rain):
        super().__init__()
        self.image = pygame.image.load("assets_dragons/full_white_alpha.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1080 / 2
        self.rect.y = 600 / 2
        self.health_cure = 10
        self.velocity = random.randint(2, 4)
        self.fish_rain = fish_rain

    def remove(self):
        self.fish_rain.alpha_white.remove(self)

    def erase(self):
        if len(self.fish_rain.all_fish) == 0:
            self.remove()
