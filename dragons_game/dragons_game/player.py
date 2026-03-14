import pygame
from projectile import Projectile
import animation


class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("toothless_hiccup_riding")
        self.game = game
        self.health = 150
        self.max_health = 150
        self.stamina = 120
        self.max_stamina = 120
        self.stamina_regeneration = 0.1
        self.fire_ball = 35
        self.stamina_fire_ball = 25
        self.velocity = 2
        self.all_projectiles = pygame.sprite.Group()
        self.lose_accelerate = 1
        self.image = pygame.transform.scale(self.image, (290, 204))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 300
        self.case = 0
        self.tired = 0

    def accelerate_check(self):
        self.lose_stamina(self.lose_accelerate)
        self.velocity = 5

    def reset_velocity(self):
        if self.stamina <= 40:
            self.velocity = 2

    def gain_health(self, amount):
        if self.health + amount <= self.max_health:
            self.health += amount

    def damage_toothless(self, amount):
        self.health -= amount
        if self.game.score - amount > 0:
            self.game.score -= amount / 2
        if self.health <= 0:
            self.game.game_over()

    def update_health_bar(self, surface):
        bar_color = (111, 210, 46)
        bar_color_bg = (210, 0, 0)

        bar_position = [self.rect.x + 45, self.rect.y - 10, self.health, 10]
        bar_position_bg = [self.rect.x + 45, self.rect.y - 10, self.max_health, 10]

        pygame.draw.rect(surface, bar_color_bg, bar_position_bg)
        pygame.draw.rect(surface, bar_color, bar_position)

    def lose_stamina(self, amount):
        self.stamina -= amount

    def gain_stamina(self):
        if self.stamina <= self.max_stamina:
            self.stamina += self.stamina_regeneration

    def stamina_update(self, surface):
        stamina_color = (201, 27, 167)
        stamina_color_bg = (191, 204, 204)

        stamina_position = [self.rect.x + 45, self.rect.y, self.stamina, 8]
        stamina_position_bg = [self.rect.x + 45, self.rect.y, self.max_stamina, 8]

        pygame.draw.rect(surface, stamina_color_bg, stamina_position_bg)
        pygame.draw.rect(surface, stamina_color, stamina_position)

    def lose_stamina_fire_ball(self):
        if self.stamina - self.stamina_fire_ball >= 0 and self.case == 0:
            self.launch_projectile()
            self.stamina -= self.stamina_fire_ball

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

    def move_right(self):
        self.rect.x += self.velocity
        if self.case == 1:
            self.image = pygame.transform.flip(self.image, True, False)
            self.case = 0

    def move_left(self):
        self.rect.x -= self.velocity
        if self.case == 0:
            self.image = pygame.transform.flip(self.image, True, False)
            self.case = 1