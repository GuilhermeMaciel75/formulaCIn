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

    #  Setters
    @x.setter
    def x(self, value):
        self._position_x = value

    @y.setter
    def y(self, value):
        self._position_y = value

    # Functions
    @staticmethod
    def randomize_position(mapa):
        linha_matriz = randint(3, 33)
        coluna_matriz = randint(3, 40)

        # O elemento da matriz sorteado é igual a 0:
        if mapa.mapa[coluna_matriz][linha_matriz] == 0:
            if mapa.mapa[coluna_matriz -1][linha_matriz] == 0 and mapa.mapa[coluna_matriz][linha_matriz - 1] == 0:
                # Se o elemento sorteado = 0, o  elemento da linha anterior e mesma coluna = 0,
                # o elemento da mesma linha e coluna anterior = 0 e o elemento da linha anterior e coluna anterior = 0
                # o item surge entre esses 4 elementos
                if mapa.mapa[coluna_matriz - 1][linha_matriz - 1] == 0:
                    coord_x = linha_matriz * 18
                    coord_y = coluna_matriz * 18
                # Se o elemento da linha anterior e coluna anterior != 0
                # o item surge entre o elemento sorteado e os seus sucessores
                else:
                    coord_x = linha_matriz * 18 + 18
                    coord_y = coluna_matriz * 18 + 18

            elif mapa.mapa[coluna_matriz + 1][linha_matriz] == 0 and mapa.mapa[coluna_matriz][linha_matriz + 1] == 0:
                #Se o elemento sorteado = 0, o elemento da linha seguinte e mesma coluna = 0,
                # o elemento da mesma linha e coluna seguinte = 0 e o elemento da linha seguinte e coluna seguinte = 0
                # o item surge entre esses 4 elementos
                if mapa.mapa[coluna_matriz + 1][linha_matriz + 1] == 0:
                    coord_x = linha_matriz * 18 + 18
                    coord_y = coluna_matriz * 18 + 18
                # Se o elemento da linha seguinte e coluna seguinte != 0
                # o item surge entre o elemento sorteado e seus antecessores
                else:
                    coord_x = linha_matriz * 18
                    coord_y = coluna_matriz * 18

            # Se algum dos elementos sucessores != 0 e algum dos elementos anteriores != 0
            # a coordenada x e a coordenada y são definidas separadamente de acordo com seus elementos adjacentes
            else:
                if mapa.mapa[coluna_matriz][linha_matriz - 1] == 0:
                    coord_x = linha_matriz * 18
                else:
                    coord_x = linha_matriz * 18 + 18
                if mapa.mapa[coluna_matriz - 1][linha_matriz] == 0:
                    coord_y = coluna_matriz * 18
                else:
                    coord_y = coluna_matriz * 18 + 18

            return [coord_x, coord_y]

        # Se o elemento sorteado for != 0, a função roda denovo até o elemento sorteado = 0
        else: return Item.randomize_position(mapa)

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
