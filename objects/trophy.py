import pygame as pg
from cronometro import contar_tempo

from objects.item import Items

class Trophy(Items):
    def __init__(self):
        super().__init__()
 
        # Trophy properties
        self.image = pg.image.load('assets/trofeu.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (20,20))
        self.rect = self.image.get_rect(center = (self._position_x, self._position_y))
 
        # Trophy functions
    def adicionar_trofeu(self, grupo):
        if contar_tempo() == 60:
            for _ in range(5):
                grupo.add(Trophy())
        elif contar_tempo() == 40:
            for _ in range(2):
                grupo.add(Trophy())
        elif contar_tempo() == 20:
            for _ in range(2):
                grupo.add(Trophy())

    def desenhar_trofeu(self, grupo, tela):
        grupo.draw(tela)
