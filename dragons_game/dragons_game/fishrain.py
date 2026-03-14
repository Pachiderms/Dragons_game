import pygame

from bewilderbeastally import BewilderbeastAlly
from fish import Fish

import random


class BewilderbeastFishRain:
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 50
        self.wave = 0
        self.all_fish = pygame.sprite.Group()
        self.alpha_white = pygame.sprite.Group()
        self.game = game
        self.rain_mode = False

    def add_percent(self):
        self.percent += self.percent_speed / 250

    def reset_percent(self):
        self.percent = 0
        self.wave += 1

    def is_full_loaded(self):
        return self.percent >= 100

    def fish_rain(self):
        n = 0
        i = random.randint(1, 15)
        while n <= i:
            self.all_fish.add(Fish(self))
            n += 1
        self.alpha_white.add(BewilderbeastAlly(self))

    def attempt_rain(self):
        if self.is_full_loaded() and len(self.game.enemies_drags) == 0:
            self.fish_rain()
            self.rain_mode = True

    def update_bar(self, surface):
        self.add_percent()

        pygame.draw.rect(surface, (0, 0, 0), [
            0,
            surface.get_height() - 10,
            surface.get_width(),
            10
        ])

        pygame.draw.rect(surface, (187, 11, 11), [
            0,
            surface.get_height() - 10,
            (surface.get_width() / 108) * self.percent,
            10
        ])
