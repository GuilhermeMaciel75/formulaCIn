import pygame as pg
from random import randint

pg.init()


class Item(pg.sprite.Sprite):
    def __init__(self, width=None, height=None, type="none") -> None:
        super().__init__()

        #  Basic Properties
        self._position_x, self._position_y = Item.randomize_position()
        self._width = width
        self._height = height
        self._type = type

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
    def randomize_position():
        coord_x = randint(3, 33) * 18 - 9
        coord_y = randint(3, 40) * 18 - 9
        return [coord_x, coord_y]

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
