from pygame.math import Vector2
from dataclasses import dataclass, field


@dataclass
class Screen:
    width: int = 1280
    height: int = 720
    tile_size: int = 64
    overlay_tool_position: tuple[int, int] = field(init=False)
    overlay_seed_position: tuple[int, int] = field(init=False)

    @property
    def size(self) -> tuple[int, int]:
        return (self.width, self.height)

    def __post_init__(self):
        self.overlay_tool_position = (40, self.height - 15)
        self.overlay_seed_position = (70, self.height - 5)


@dataclass
class PlayerToolOffset:
    left: Vector2 = field(default_factory=lambda: Vector2(-50, 40))
    right: Vector2 = field(default_factory=lambda: Vector2(50, 40))
    up: Vector2 = field(default_factory=lambda: Vector2(0, -10))
    down: Vector2 = field(default_factory=lambda: Vector2(0, 50))


@dataclass
class Layers:
    water: int = 0
    ground: int = 1
    soil: int = 2
    soil_water: int = 3
    rain_floor: int = 4
    house_bottom: int = 5
    ground_plant: int = 6
    main: int = 7
    house_top: int = 8
    fruit: int = 9
    rain_drops: int = 10

    def get(self, name: str) -> int:
        return getattr(self, name.replace(" ", "_"))


@dataclass
class ApplePositions:
    small: list[tuple[int, int]] = (
        (18, 17),
        (30, 37),
        (12, 50),
        (30, 45),
        (20, 30),
        (30, 10),
    )
    large: list[tuple[int, int]] = (
        (30, 24),
        (60, 65),
        (50, 50),
        (16, 40),
        (45, 50),
        (42, 70),
    )

    def get(self, size: str) -> list[tuple[int, int]]:
        return getattr(self, size.lower())


@dataclass
class GrowSpeed:
    corn: float = 1.0
    tomato: float = 0.7

    def get(self, crop: str) -> float:
        return getattr(self, crop)


@dataclass
class SalePrices:
    wood: int = 4
    apple: int = 2
    corn: int = 10
    tomato: int = 20

    def get(self, item: str) -> int:
        return getattr(self, item)


@dataclass
class PurchasePrices:
    corn: int = 4
    tomato: int = 5

    def get(self, item: str) -> int:
        return getattr(self, item)


@dataclass
class Graphics:
    animation_speed: int = 4


@dataclass
class Settings:
    screen: Screen = field(default_factory=lambda: Screen())
    player_tool_offset: PlayerToolOffset = field(
        default_factory=lambda: PlayerToolOffset()
    )
    layers: Layers = field(default_factory=lambda: Layers())
    apple_positions: ApplePositions = field(default_factory=lambda: ApplePositions())
    grow_speed: GrowSpeed = field(default_factory=lambda: GrowSpeed())
    sales_prices: SalePrices = field(default_factory=lambda: SalePrices())
    purchase_prices: PurchasePrices = field(default_factory=lambda: PurchasePrices())
    graphics: Graphics = field(default_factory=lambda: Graphics())
