import pygame, sys
from pydew.settings import Settings
from pydew.level import Level
from pydew.support import import_folder


class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.screen.size)
        self.import_assets()

        self.clock = pygame.time.Clock()
        self.level = Level(settings=self.settings, animations=self.animations)

    def import_assets(self):
        self.animations: dict[str, list[pygame.Surface]] = {
            "up": [],
            "down": [],
            "left": [],
            "right": [],
            "right_idle": [],
            "left_idle": [],
            "up_idle": [],
            "down_idle": [],
            "right_hoe": [],
            "left_hoe": [],
            "up_hoe": [],
            "down_hoe": [],
            "right_axe": [],
            "left_axe": [],
            "up_axe": [],
            "down_axe": [],
            "right_water": [],
            "left_water": [],
            "up_water": [],
            "down_water": [],
        }
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(
                "src", "pydew", "graphics", "character", animation
            )

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
