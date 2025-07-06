import pygame
from pydew.settings import Settings
from pydew.player import Player
from pydew.overlay import Overlay
from pydew.camera import Camera
from pytmx.util_pygame import load_pygame

from os.path import join
from pydew.sprites import Generic, Water, Flower, Tree
from typing import Optional


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

        def create_generic_tiles(layer: str, layer_index: Optional[str] = None):
            for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():
                Generic(
                    settings=self.settings,
                    pos=(
                        x * self.settings.screen.tile_size,
                        y * self.settings.screen.tile_size,
                    ),
                    surf=surf,
                    groups=self.all_sprites,
                    z_level=layer_index,
                )

        def create_water():
            for x, y, _ in tmx_data.get_layer_by_name("Water").tiles():
                Water(
                    settings=self.settings,
                    pos=(
                        x * self.settings.screen.tile_size,
                        y * self.settings.screen.tile_size,
                    ),
                    frames=self.animations["water"],
                    z_level="ground",
                    groups=[self.all_sprites],
                )

        def create_flowers():
            for obj in tmx_data.get_layer_by_name("Decoration"):
                Flower(
                    settings=self.settings,
                    pos=(obj.x, obj.y),
                    surf=obj.image,
                    groups=[self.all_sprites],
                )

        def create_trees():
            for obj in tmx_data.get_layer_by_name("Trees"):
                Tree(
                    settings=self.settings,
                    pos=(obj.x, obj.y),
                    surf=obj.image,
                    groups=[self.all_sprites],
                    size=obj.name,
                )

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

        for layer in ["HouseFloor", "HouseFurnitureBottom"]:
            create_generic_tiles(layer, "house_bottom")

        for layer in ["HouseWalls", "HouseFurnitureTop", "Fence"]:
            create_generic_tiles(layer)

        create_water()
        create_flowers()
        create_trees()

    def setup(self):
        self.player = Player(
            group=self.all_sprites,
            pos=(430, 320),
            settings=self.settings,
            animations=self.animations["player"],
        )

        self.load_tilemap()

    def run(self, dt: float):
        self.display_surface.fill("black")
        self.all_sprites.draw(self.player)
        self.all_sprites.update(dt)
        self.overlay.display()
