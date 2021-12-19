import pygame as pg
from objects.item import Item

class Banana(Item):
    def __init__(self, mapa):
        super().__init__(mapa)

        # Propriedades da Banana
        self.image = pg.image.load('assets/banana.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect(center=(self._posicao_x, self._posicao_y))
