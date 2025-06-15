import pygame
from pydew.settings import Settings
from pydew.player import Player


class Level:
    def __init__(self, settings: Settings):
        self.settings = settings

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        self.player = Player(
            group=self.all_sprites, pos=(430, 320), settings=self.settings
        )

    def run(self, dt: float):
        self.display_surface.fill("black")
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
