import pygame as pg

from objects.item import Items

class Banana(Items):
    def __init__(self):
        super().__init__()
 
        # Banana properties
        self.image = pg.image.load('assets/banana.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect(center = (self._position_x, self._position_y))
        self.creation_time = pg.time.get_ticks()
 
        # Banana functions
        #def timer(self):
        #    actual_time = pg.time.get_ticks()
        #    if actual_time - self.creation_time >= destruction_time:
        #        super().destroy()