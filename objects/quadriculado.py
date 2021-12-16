import pygame as pg

pg.init()

class Quadriculado(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self._x = x
        self._y = y
        self.image = pg.image.load('assets/mapa/quadriculado_vermelho.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (18, 18))
        self.rect = self.image.get_rect(topleft=(self._x, self._y))