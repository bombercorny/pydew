import pygame
from pydew.player import Player
from pydew.settings import Settings
from dataclasses import dataclass, field
from os.path import join


@dataclass
class Overlay:
    player: Player
    display_surface: pygame.Surface
    settings: Settings
    overlay_path: str = join("src", "pydew", "graphics", "overlay")
    tool_surfaces: dict[str, pygame.Surface] = field(init=False)
    seed_surfaces: dict[str, pygame.Surface] = field(init=False)

    def __post_init__(self):
        self.tool_surfaces = {
            tool: pygame.image.load(
                join(self.overlay_path, f"{tool}.png")
            ).convert_alpha()
            for tool in self.player.tools
        }
        self.seed_surfaces = {
            seed: pygame.image.load(
                join(self.overlay_path, f"{seed}.png")
            ).convert_alpha()
            for seed in self.player.seeds
        }

    @property
    def tool_surface(self) -> pygame.Surface:
        return self.tool_surfaces[self.player.selected_tool]

    @property
    def tool_rect(self) -> pygame.FRect:
        return self.tool_surface.get_frect(
            midbottom=self.settings.screen.overlay_tool_position
        )

    @property
    def seed_surface(self) -> pygame.Surface:
        return self.seed_surfaces[self.player.selected_seed]

    @property
    def seed_rect(self) -> pygame.FRect:
        return self.seed_surface.get_frect(
            midbottom=self.settings.screen.overlay_seed_position
        )

    def display(self):
        self.display_surface.blit(self.tool_surface, self.tool_rect)
        self.display_surface.blit(self.seed_surface, self.seed_rect)
