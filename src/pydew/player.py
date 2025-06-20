import pygame
from pygame.math import Vector2
from pydew.settings import Settings
from pydew.timer import Timer


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

        self.timers: dict[str, Timer] = {
            "tool_use": Timer(350, self.use_tool),
            "tool_switch": Timer(200),
            "seed_use": Timer(350, self.use_seed),
            "seed_switch": Timer(200),
        }

        # tools
        self.tools = ["hoe", "axe", "water"]
        self.tool_index = 0

        # seeds
        self.seeds = ["corn", "tomato"]
        self.seed_index = 0

    @property
    def selected_tool(self) -> str:
        return self.tools[self.tool_index % len(self.tools)]

    @property
    def selected_seed(self) -> str:
        return self.seeds[self.seed_index % len(self.seeds)]

    def use_tool(self):
        pass

    def use_seed(self):
        pass

    def update_status(self):
        if self.direction.magnitude() == 0:
            self.status = f"{self.status.split('_')[0]}_idle"

        if self.timers["tool_use"].active:
            self.status = f"{self.status.split('_')[0]}_{self.selected_tool}"

    def input(self):
        keys = pygame.key.get_pressed()

        if not self.timers["tool_use"].active:
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

            # tool use
            if keys[pygame.K_SPACE]:
                self.timers["tool_use"].activate()
                self.direction = Vector2()  # stop player movement on tool usage
                self.frame_index = 0  # reset to get consistent animations

            # switch tool
            if (
                keys[pygame.K_q] and not self.timers["tool_switch"].active
            ):  # prevent multiple switches per frame
                self.timers["tool_switch"].activate()
                self.tool_index += 1

            # seed use
            if keys[pygame.K_LCTRL]:
                self.timers["seed_use"].activate()
                self.direction = Vector2()  # stop player movement on seed usage
                self.frame_index = 0  # reset to get consistent animations

            # switch seed
            if (
                keys[pygame.K_e] and not self.timers["seed_switch"].active
            ):  # prevent multiple switches per frame
                self.timers["seed_switch"].activate()
                self.seed_index += 1

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

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def update(self, dt: float):
        self.update_timers()
        self.input()
        self.move(dt)
        self.update_status()
        self.animate(dt)
