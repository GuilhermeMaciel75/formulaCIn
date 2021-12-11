import pygame as pg

from objects.item import Items

class Lightning(Items):
    def __init__(self):
        super().__init__()
 
        # Lightning properties
        self.image = pg.image.load('assets/raio.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect(center = (self._position_x, self._position_y))
        self.creation_time = pg.time.get_ticks()
 
        # Lightning functions
        #def timer(self):
        #    actual_time = pg.time.get_ticks()
        #    if actual_time - self.creation_time >= destruction_time:
        #        super().destroy()