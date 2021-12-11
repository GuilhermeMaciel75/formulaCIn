import pygame as pg
from random import randint
 
pg.init()
 
class Items(pg.sprite.Sprite):
    def __init__(self, width=None, height=None, type="none") -> None:
        super().__init__()
 
        #  Basic Properties
        self._position_x, self._position_y = Items.randomize_position()
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
    def randomize_position():
        coord_x = randint(30,970)
        coord_y = randint(30,470)
        return [coord_x, coord_y]
 
    def item_collision(self):
        pass
 
    def draw(self):
        pass
 
    def destroy(self):
        pass
 
    def update(self):
        pass