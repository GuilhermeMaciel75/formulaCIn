import pygame as pg
from random import randint

pg.init()

class Item(pg.sprite.Sprite):
    def __init__(self, mapa) -> None:
        super().__init__()

        # Propriedades básicas
        self._posicao_x, self._posicao_y = Item.randomizar_posicao(mapa)

    # Getters
    @property
    def x(self):
        return self._posicao_x

    @property
    def y(self):
        return self._posicao_y

    # Setters
    @x.setter
    def x(self, value):
        self._posicao_x = value

    @y.setter
    def y(self, value):
        self._posicao_y = value

    # Funções
    @staticmethod
    def randomizar_posicao(mapa):
        linha_matriz = randint(3, 33)
        coluna_matriz = randint(3, 40)

        # O elemento da matriz sorteado é igual a 0:
        if mapa.mapa[coluna_matriz][linha_matriz] == 0:
            # Verifica o elemento sorteado forma um espaço 2X2 de pistas (0) com alguma de suas diagonais
            # e se sim, retorna a posição do item entre essas 4 pistas
            if mapa.mapa[coluna_matriz - 1][linha_matriz] == 0 and mapa.mapa[coluna_matriz][linha_matriz - 1] == 0\
            and mapa.mapa[coluna_matriz - 1][linha_matriz - 1] == 0:
                coord_x = linha_matriz * 18
                coord_y = coluna_matriz * 18
                return [coord_x, coord_y]

            elif mapa.mapa[coluna_matriz - 1][linha_matriz] == 0 and mapa.mapa[coluna_matriz][linha_matriz + 1] == 0\
            and mapa.mapa[coluna_matriz - 1][linha_matriz + 1] == 0:
                coord_x = linha_matriz * 18 + 18
                coord_y = coluna_matriz * 18
                return [coord_x, coord_y]

            elif mapa.mapa[coluna_matriz + 1][linha_matriz] == 0 and mapa.mapa[coluna_matriz][linha_matriz + 1] == 0\
            and mapa.mapa[coluna_matriz + 1][linha_matriz + 1] == 0:
                coord_x = linha_matriz * 18 + 18
                coord_y = coluna_matriz * 18 + 18
                return [coord_x, coord_y]

            elif mapa.mapa[coluna_matriz + 1][linha_matriz] == 0 and mapa.mapa[coluna_matriz][linha_matriz - 1] == 0\
            and mapa.mapa[coluna_matriz + 1][linha_matriz - 1] == 0:
                coord_x = linha_matriz * 18
                coord_y = coluna_matriz * 18 + 18
                return [coord_x, coord_y]

            else: return Item.randomizar_posicao(mapa)

        # Se o elemento sorteado for != 0, a função roda denovo até o elemento sorteado = 0
        else: return Item.randomizar_posicao(mapa)

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
