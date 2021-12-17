import pygame as pg

from objects.item import Item


class Lightning(Item):
    def __init__(self, mapa):
        super().__init__(mapa)

        # Lightning properties
        self.image = pg.image.load('assets/raio.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(self._position_x, self._position_y))
