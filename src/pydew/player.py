import pygame
from pygame.math import Vector2
from pydew.settings import Settings


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], group, settings: Settings):
        super().__init__(group)
        self.settings = settings
        self.image = pygame.Surface((32, 64))
        self.image.fill("red")
        self.rect = self.image.get_frect(center=pos)
        self.direction = Vector2()
        self.speed = 200

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, dt: float):
        if self.direction.magnitude() > 0:
            # horizontal
            self.rect.x += self.direction.x * dt * self.speed
            # vertical
            self.rect.y += self.direction.y * dt * self.speed

    def update(self, dt: float):
        self.move(dt)
        self.input()
