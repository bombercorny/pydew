import pygame
from typing import Optional
from pydew.settings import Settings


class Generic(pygame.sprite.Sprite):
    def __init__(
        self,
        settings: Settings,
        pos: tuple[int, int],
        surf: pygame.Surface,
        groups,
        z_level: Optional[str] = None,
    ):
        super().__init__(groups)
        self.settings = settings
        self.image = surf
        self.rect = self.image.get_frect(topleft=pos)

        if not z_level:
            z_level = "main"
        self.layer_index = self.settings.layers.get(z_level)


class Water(Generic):
    def __init__(
        self,
        settings: Settings,
        pos: tuple[int, int],
        frames: list[pygame.Surface],
        groups,
        z_level: Optional[str],
    ):
        self.frames = frames
        self.frame_index = 0

        super().__init__(
            settings=settings,
            pos=pos,
            surf=self.frames[self.frame_index],
            groups=groups,
        )

    def animate(self, dt: float):
        self.frame_index += self.settings.graphics.animation_speed * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        self.image = self.frames[int(self.frame_index)]

    def update(self, dt: float):
        self.animate(dt)


class Flower(Generic):
    def __init__(
        self,
        settings: Settings,
        pos: tuple[int, int],
        surf: pygame.Surface,
        groups,
    ):
        super().__init__(
            settings=settings,
            pos=pos,
            surf=surf,
            groups=groups,
        )


class Tree(Generic):
    def __init__(
        self,
        settings: Settings,
        pos: tuple[int, int],
        surf: pygame.Surface,
        groups,
        size: str,
    ):
        super().__init__(
            settings=settings,
            pos=pos,
            surf=surf,
            groups=groups,
        )
        self.size = size
