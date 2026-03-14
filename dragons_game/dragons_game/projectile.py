import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load("assets_dragons/fireblast.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 250
        self.rect.y = player.rect.y + 145
        self.origin_image = self.image
        self.angle = 0
        self.left = 0

    def rotate(self):
        if self.left == 1:
            self.image = pygame.transform.flip(self.image, True, False)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.left = 0
        self.rect.x += self.velocity

        for enemy_dragons in self.player.game.check_collision(self, self.player.game.enemies_drags):
            self.remove()
            enemy_dragons.damage(self.player.fire_ball)

        if self.rect.x >= 980:
            self.remove()

        if self.rect.x <= 0:
            self.remove()