import pygame
from pygame.math import Vector2
from pydew.settings import Settings


class Camera(pygame.sprite.Group):
    def __init__(self, display_surface: pygame.Surface, settings: Settings):
        super().__init__()
        self.display_surface = display_surface
        self.settings = settings
        self.offset = pygame.math.Vector2()

    @property
    def _sprites(self) -> list[pygame.sprite.Sprite]:
        return sorted(self.sprites(), key=lambda x: x.layer_index)

    def draw(self, player):
        self.offset.x = player.rect.centerx - self.settings.screen.width / 2
        self.offset.y = player.rect.centery - self.settings.screen.height / 2

        for sprite in self._sprites:
            offset_rect = sprite.rect.copy()
            offset_rect.center -= self.offset
            self.display_surface.blit(sprite.image, offset_rect)
