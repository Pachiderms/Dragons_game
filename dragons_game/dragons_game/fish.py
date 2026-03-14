import pygame
import random

from enemies import Razorwhip, Gronk
from enemies import HideuxBraguettaure


class Fish(pygame.sprite.Sprite):
    def __init__(self, fish_rain):
        super().__init__()
        self.image = pygame.image.load("assets_dragons/fish.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(10, 900)
        self.rect.y = random.randint(600, 1000)
        self.health_cure = 3
        self.velocity = random.randint(1, 4)
        self.fish_rain = fish_rain

    def remove(self):
        self.fish_rain.all_fish.remove(self)

        if len(self.fish_rain.all_fish) == 0:
            self.fish_rain.reset_percent()
            self.fish_rain.alpha_white.remove()
            self.fish_rain.rain_mode = False
            n = random.randint(1, 4)

            if n == 1:
                self.fish_rain.game.enemies_spawn(HideuxBraguettaure)
                self.fish_rain.game.enemies_spawn(HideuxBraguettaure)
                if self.fish_rain.wave >= 5:
                    self.fish_rain.game.enemies_spawn(Razorwhip)
            elif n == 2:
                self.fish_rain.game.enemies_spawn(HideuxBraguettaure)
                self.fish_rain.game.enemies_spawn(HideuxBraguettaure)
                if self.fish_rain.wave >= 3:
                    self.fish_rain.game.enemies_spawn(Gronk)
            elif n == 3:
                self.fish_rain.game.enemies_spawn(Gronk)
                self.fish_rain.game.enemies_spawn(Gronk)
                if self.fish_rain.wave >= 5:
                    self.fish_rain.game.enemies_spawn(Razorwhip)

            elif n == 4:
                self.fish_rain.game.enemies_spawn(HideuxBraguettaure)
                self.fish_rain.game.enemies_spawn(HideuxBraguettaure)
                if self.fish_rain.wave >= 5:
                    self.fish_rain.game.enemies_spawn(Razorwhip)
                if self.fish_rain.wave >= 3:
                    self.fish_rain.game.enemies_spawn(Gronk)

    def fall(self):
        self.rect.y -= self.velocity

        if self.rect.y <= 0:
            self.remove()

            if len(self.fish_rain.all_fish) == 0:
                self.fish_rain.reset_percent()
                self.fish_rain.rain_mode = False

        if self.fish_rain.game.check_collision(self, self.fish_rain.game.all_player):
            self.remove()
            self.fish_rain.game.player.gain_health(self.health_cure)