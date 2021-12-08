import pygame as pg

pg.init()


class Item:

    def __init__(self, position_x=None, position_y=None, width=None, height=None, name="none") -> None:
        """Create an item with
            position_x (int): Horizontal Position
            position_y (int): Vertical Position
            width (int): Width at Object, relative to screen
            height (int): Heignt at Object, relative to screen
        """

        #  Basic Properties
        self._position_x = position_x
        self._position_y = position_y
        self._width = width
        self._height = height
        self._name = name

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
    def name(self):
        return self._name

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
