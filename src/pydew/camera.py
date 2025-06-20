import pygame


class Camera(pygame.sprite.Group):
    def __init__(self, display_surface: pygame.Surface):
        super().__init__()
        self.display_surface = display_surface

    @property
    def _sprites(self) -> list[pygame.sprite.Sprite]:
        return self.sprites()

    def draw(self):
        for sprite in self._sprites:
            self.display_surface.blit(sprite.image, sprite.rect)
