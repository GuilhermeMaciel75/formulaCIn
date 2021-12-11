import pygame as pg

from objects.item import Items

class Trophy(Items):
    def __init__(self):
        super().__init__()
 
        # Trophy properties
        self.image = pg.image.load('assets/trofeu.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect(center = (self._position_x, self._position_y))
 
        # Trophy functions