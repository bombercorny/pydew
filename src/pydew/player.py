import pygame
from pygame.math import Vector2
from pydew.settings import Settings


class Player(pygame.sprite.Sprite):
    def __init__(
        self,
        pos: tuple[int, int],
        group,
        settings: Settings,
        animations: dict[str, list[pygame.Surface]],
    ):
        super().__init__(group)
        self.settings = settings
        self.animations = animations

        self.status = "down"
        self.frame_index = 0

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_frect(center=pos)
        self.direction = Vector2()
        self.speed = 200
        self.animations = animations

    def update_status(self):
        if self.direction.magnitude() == 0:
            self.status = f"{self.status.split('_')[0]}_idle"

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = "up"
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = "down"
        else:
            self.direction.y = 0
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = "left"
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = "right"
        else:
            self.direction.x = 0

    def move(self, dt: float):
        if self.direction.magnitude() > 0:
            # horizontal
            self.rect.x += self.direction.x * dt * self.speed
            # vertical
            self.rect.y += self.direction.y * dt * self.speed

    def animate(self, dt: float):
        self.frame_index += self.settings.graphics.animation_speed * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]

    def update(self, dt: float):
        self.input()
        self.move(dt)
        self.update_status()
        self.animate(dt)
