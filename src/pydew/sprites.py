import pygame
from pydew.settings import Settings


class Generic(pygame.sprite.Sprite):
    def __init__(
        self,
        settings: Settings,
        pos: tuple[int, int],
        surf: pygame.Surface,
        groups,
        z_level: str = "main",
    ):
        super().__init__(groups)
        self.settings = settings
        self.image = surf
        self.rect = self.image.get_frect(topleft=pos)
        self.layer_index = self.settings.layers.get(z_level)
