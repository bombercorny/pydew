from os import walk
from os.path import join
import pygame


def import_folder(*path: str) -> list[pygame.Surface]:
    frames = []
    for folder_path, _, image_names in walk(join(*path)):
        for image_name in sorted(image_names, key=lambda name: int(name.split(".")[0])):
            full_path = join(folder_path, image_name)
            image_surf = pygame.image.load(full_path).convert_alpha()
            frames.append(image_surf)
    return frames
