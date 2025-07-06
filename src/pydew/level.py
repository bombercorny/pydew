import pygame
from pydew.settings import Settings
from pydew.player import Player
from pydew.overlay import Overlay
from pydew.camera import Camera
from pytmx.util_pygame import load_pygame

from os.path import join
from pydew.sprites import Generic


class Level:
    def __init__(self, settings: Settings, animations: dict[str, list[pygame.Surface]]):
        self.settings = settings
        self.animations = animations

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = Camera(
            display_surface=self.display_surface, settings=self.settings
        )

        self.setup()
        self.overlay = Overlay(
            player=self.player,
            display_surface=self.display_surface,
            settings=self.settings,
        )

    def load_tilemap(self):
        tmx_data = load_pygame(join("src", "pydew", "data", "map.tmx"))

        # map
        self.floor = Generic(
            settings=self.settings,
            pos=(0, 0),
            surf=pygame.image.load(
                join("src", "pydew", "graphics", "world", "ground.png")
            ),
            z_level="ground",
            groups=[self.all_sprites],
        )

        # house
        # for x, y, surf in tmx_data.get_layer_by_name("HouseFurnitureBottom").tiles():
        #     print(x, y)

    def setup(self):
        self.player = Player(
            group=self.all_sprites,
            pos=(430, 320),
            settings=self.settings,
            animations=self.animations,
        )

        self.load_tilemap()

    def run(self, dt: float):
        self.display_surface.fill("black")
        self.all_sprites.draw(self.player)
        self.all_sprites.update(dt)
        self.overlay.display()
