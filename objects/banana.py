import pygame as pg

from objects.item import Item


class Banana(Item):
    def __init__(self):
        super().__init__()

        # Banana properties
        self.image = pg.image.load('assets/banana.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect(center=(self._position_x, self._position_y))
