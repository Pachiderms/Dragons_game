import pygame
from player import Player
from enemies import EnemyDragons, HideuxBraguettaure, Razorwhip, Gronk
from fishrain import BewilderbeastFishRain
import random


class Game:

    def __init__(self):

        self.is_playing = False
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        self.enemies_drags = pygame.sprite.Group()
        self.fish_rain = BewilderbeastFishRain(self)
        self.best_score = 0
        self.score = 0
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.player.all_projectiles = pygame.sprite.Group()
        self.player.case = 0
        self.player.rect.x = 0
        self.player.rect.y = 300
        self.player.stamina = 100
        self.player.max_stamina = 100
        n = random.randint(1, 3)

        if n == 1:
            self.enemies_spawn(HideuxBraguettaure)
            self.enemies_spawn(HideuxBraguettaure)
            if self.fish_rain.wave >= 5:
                self.enemies_spawn(Razorwhip)
        elif n == 2:
            self.enemies_spawn(HideuxBraguettaure)
            self.enemies_spawn(HideuxBraguettaure)
            if self.fish_rain.wave >= 3:
                self.enemies_spawn(Gronk)
        elif n == 3:
            self.enemies_spawn(Gronk)
            self.enemies_spawn(Gronk)
            if self.fish_rain.wave >= 5:
                self.enemies_spawn(Razorwhip)

        elif n == 4:
            self.enemies_spawn(HideuxBraguettaure)
            self.enemies_spawn(HideuxBraguettaure)
            if self.fish_rain.wave >= 5:
                self.enemies_spawn(Razorwhip)
            if self.fish_rain.wave >= 3:
                self.enemies_spawn(Gronk)

    def game_over(self):
        self.is_playing = False

        self.enemies_drags = pygame.sprite.Group()

        self.player.health = self.player.max_health
        self.player.stamina = self.player.max_stamina
        self.player.stamina_regeneration = 0.1

        if self.best_score < self.score:
            self.best_score = self.score
        self.score = 0

    def update(self, screen):
        font = pygame.font.SysFont("monospace", 15)
        score_text = font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))
        screen.blit(self.player.image, self.player.rect)

        self.player.stamina_update(screen)

        self.player.update_health_bar(screen)
        self.player.gain_stamina()
        self.player.reset_velocity()

        self.fish_rain.update_bar(screen)

        for projectile in self.player.all_projectiles:
            projectile.move()

        self.player.all_projectiles.draw(screen)

        for enemy_dragon in self.enemies_drags:
            enemy_dragon.update_health_bar(screen)
            enemy_dragon.movement()
            self.enemies_drags.draw(screen)

        for fish in self.fish_rain.all_fish:
            fish.fall()

        for ally in self.fish_rain.alpha_white:
            ally.erase()

        self.fish_rain.all_fish.draw(screen)
        self.fish_rain.alpha_white.draw(screen)

        if self.pressed.get(pygame.K_UP) and self.player.rect.y > 50:
            self.player.move_up()
        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y < 380:
            self.player.move_down()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        elif self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 780:
            self.player.move_right()
        elif self.pressed.get(pygame.K_a):
            self.player.accelerate_check()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def enemies_spawn(self, monster_name):
        self.enemies_drags.add(monster_name.__call__(self))