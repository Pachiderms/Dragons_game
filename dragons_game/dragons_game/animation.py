import pygame


class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name, size=(290, 204)):
        super().__init__()
        self.image = pygame.image.load(f"assets_dragons/{sprite_name}.png")
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
