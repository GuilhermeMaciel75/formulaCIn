import pygame as pg
from random import randint
from cronometro import contar_tempo

from objects.banana import Banana
from objects.lightning import Lightning
 
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
        coord_x = randint(58,602)
        coord_y = randint(58,728)
        return [coord_x, coord_y]
 
    def item_collision(self):
        pass
 
    def destroy(self):
        pass
 
    def update(self):
        pass

    def randomizar_item(self):
        if randint(1,2) == 1:
            item = "banana"
        else:
            item = "raio"

        return item

    #Adiciona os sprites à seus respectivos grupos
    def adicionar_powerups(self, grupo):
        if contar_tempo() == 60:
            for _ in range(3):
                if self.randomizar_item() == "banana":
                    grupo.add(Banana())
                else:
                    grupo.add(Lightning())
        elif contar_tempo() == 40:
            if self.randomizar_item() == "banana":
                grupo.add(Banana())
            else:
                grupo.add(Lightning())
        elif contar_tempo() == 20:
            if self.randomizar_item() == "banana":
                grupo.add(Banana())
            else:
                grupo.add(Lightning())

    def desenhar_powerups(self, grupo, tela):
                grupo.draw(tela)