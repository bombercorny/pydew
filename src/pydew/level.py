import pygame
from pydew.settings import Settings
from pydew.player import Player
from pydew.overlay import Overlay


class Level:
    def __init__(self, settings: Settings, animations: dict[str, list[pygame.Surface]]):
        self.settings = settings
        self.animations = animations

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()

        self.setup()
        self.overlay = Overlay(
            player=self.player,
            display_surface=self.display_surface,
            settings=self.settings,
        )

    def setup(self):
        self.player = Player(
            group=self.all_sprites,
            pos=(430, 320),
            settings=self.settings,
            animations=self.animations,
        )

    def run(self, dt: float):
        self.display_surface.fill("black")
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
        self.overlay.display()
