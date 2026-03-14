import pygame
import random
from projectile import Projectile
import animation


class EnemyDragons(animation.AnimateSprite):

    def __init__(self, game, name, size):
        super().__init__(name, size)
        self.game = game
        self.dam = 0
        self.rect = self.image.get_rect()
        self.rect.x = 1080
        self.rect.y = random.randint(110, 415)

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, self.default_speed)

    def respawn(self):
        self.rect.x = 1080
        self.rect.y = random.randint(110, 415)
        self.velocity = random.randint(1, self.default_speed)
        self.health = self.max_health

    def damage(self, amount):
        self.dam = amount
        self.health -= amount
        self.game.score += amount

        if self.health <= 0:
            self.respawn()

            if self.game.fish_rain.is_full_loaded():
                self.game.enemies_drags.remove(self)

                self.game.fish_rain.attempt_rain()

    def update_health_bar(self, surface):
        bar_color = (210, 0, 0)
        bar_color_bg = (81, 85, 79)

        bar_position = [self.rect.x, self.rect.y - 10, self.health, 10]
        bar_position_bg = [self.rect.x, self.rect.y - 10, self.max_health, 10]

        pygame.draw.rect(surface, bar_color_bg, bar_position_bg)
        pygame.draw.rect(surface, bar_color, bar_position)

    def movement(self):
        self.rect.x -= self.velocity

        if self.rect.x <= 0:
            self.respawn()

        if self.game.check_collision(self, self.game.all_player):
            self.game.player.damage_toothless(self.attack)


class HideuxBraguettaure(EnemyDragons):
    def __init__(self, game):
        super().__init__(game, "Hideux_Braguettaure", (302, 193))
        self.health = 50
        self.max_health = 50
        self.set_speed(3)
        self.attack = 0.2


class Razorwhip(EnemyDragons):
    def __init__(self, game):
        super().__init__(game, "razorwhip", (289, 149))
        self.health = 100
        self.max_health = 100
        self.set_speed(1)
        self.attack = 0.4


class Gronk(EnemyDragons):
    def __init__(self, game):
        super().__init__(game, "gronk", (227, 189))
        self.health = 75
        self.max_health = 75
        self.set_speed(1)
        self.attack = 0.1
