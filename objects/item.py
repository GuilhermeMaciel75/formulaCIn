import pygame as pg
from random import randint
from cronometro import contar_tempo
 
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
        coord_x = randint(58,602)
        coord_y = randint(58,728)
        return [coord_x, coord_y]

    @staticmethod
    def item_collision():
        pass

    @staticmethod
    def destroy():
        pass

    @staticmethod
    def update():
        pass

    @staticmethod
    def randomizar_item():
        if randint(1,2) == 1:
            item = "banana"
        else:
            item = "raio"

        return item

    #Adiciona os sprites à seus respectivos grupos
    @staticmethod
    def adicionar_powerups(grupo, contador):
        if contar_tempo() == 60 and contador == 3:
            for _ in range(3):
                if Item.randomizar_item() == "banana":
                    grupo.add(Banana())
                else:
                    grupo.add(Lightning())
            return contador - 1
        elif contar_tempo() == 40 and contador == 2:
            if Item.randomizar_item() == "banana":
                grupo.add(Banana())
            else:
                grupo.add(Lightning())
            return contador - 1
        elif contar_tempo() == 20 and contador == 1:
            if Item.randomizar_item() == "banana":
                grupo.add(Banana())
            else:
                grupo.add(Lightning())
            return contador - 1
        else: return contador
    @staticmethod
    def desenhar_powerups(grupo, tela):
        grupo.draw(tela)


class Lightning(Item):
    def __init__(self):
        super().__init__()
 
        # Lightning properties
        self.image = pg.image.load('assets/raio.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect(center = (self._position_x, self._position_y))


class Banana(Item):
    def __init__(self):
        super().__init__()
 
        # Banana properties
        self.image = pg.image.load('assets/banana.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (25,25))
        self.rect = self.image.get_rect(center = (self._position_x, self._position_y))


class Trophy(Item):
    def __init__(self):
        super().__init__()
 
        # Trophy properties
        self.image = pg.image.load('assets/trofeu.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (20,20))
        self.rect = self.image.get_rect(center = (self._position_x, self._position_y))
 
        # Trophy functions
    @staticmethod
    def adicionar_trofeu(grupo, contador):
        if contar_tempo() == 60 and contador == 3:
            for _ in range(5):
                grupo.add(Trophy())
            return contador - 1
        elif contar_tempo() == 40 and contador == 2:
            for _ in range(2):
                grupo.add(Trophy())
            return contador - 1
        elif contar_tempo() == 20 and contador == 1:
            for _ in range(2):
                grupo.add(Trophy())
            return contador - 1
        else: return contador

    @staticmethod
    def desenhar_trofeu(grupo, tela):
        grupo.draw(tela)
