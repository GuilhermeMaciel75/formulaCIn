import pygame as pg
from random import randint

from mapa import Mapa

pg.init()


class Item(pg.sprite.Sprite):
    def __init__(self, mapa) -> None:
        super().__init__()

        #  Basic Properties
        self._position_x, self._position_y = Item.randomize_position(mapa)

    #  Getters
    @property
    def x(self):
        return self._position_x

    @property
    def y(self):
        return self._position_y

    @property
    def w(self):
        return self._width

    @property
    def h(self):
        return self._height

    @property
    def type(self):
        return self._type

    #  Setters
    @x.setter
    def x(self, value):
        self._position_x = value

    @y.setter
    def y(self, value):
        self._position_y = value

    @w.setter
    def w(self, value):
        self._width = value

    @h.setter
    def h(self, value):
        self._height = value

    # Functions
    @staticmethod
    def randomize_position(mapa):
        linha_matriz = randint(3, 33)
        coluna_matriz = randint(3, 40)
        if mapa.mapa[coluna_matriz][linha_matriz] == 0:
            coord_x = linha_matriz * 18 + 9
            coord_y = coluna_matriz * 18 + 9
            return [coord_x, coord_y]
        else:
            return Item.randomize_position(mapa)

    @staticmethod
    def randomizar_item():
        if randint(1, 2) == 1:
            item = "banana"
        else:
            item = "raio"

        return item

    @staticmethod
    def desenhar_item(grupo, tela):
        grupo.draw(tela)
