import pygame as pg
from cronometro import contar_tempo

from objects.item import Item


class Trophy(Item):
    def __init__(self):
        super().__init__()

        # Trophy properties
        self.image = pg.image.load('assets/trofeu.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect(center=(self._position_x, self._position_y))

    # Trophy functions
    @staticmethod
    def adicionar_trofeu(grupo, contador):
        if contar_tempo() == 60 and contador == 3:
            for _ in range(50):
                grupo.add(Trophy())
            return contador - 1
        elif contar_tempo() == 40 and contador == 2:
            for _ in range(2):
                grupo.add(Trophy())
            return contador - 1
        elif contar_tempo() == 20 and contador == 1:
            for _ in range(2):
                grupo.add(Trophy())
            return contador - 1
        else:
            return contador

