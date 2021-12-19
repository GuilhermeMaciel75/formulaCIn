import pygame as pg
from cronometro import contar_tempo

from objects.item import Item


class Trofeu(Item):
    def __init__(self, mapa):
        super().__init__(mapa)

        # Propriedades do Trofeu
        self.image = pg.image.load('assets/trofeu.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect(center=(self._posicao_x, self._posicao_y))

    # Funções
    @staticmethod
    def adicionar_trofeu(grupo, contador, mapa, tempo_inicial):
        if contar_tempo(tempo_inicial) == 60 and contador == 3:
            for _ in range(7):
                grupo.add(Trofeu(mapa))
            return contador - 1
        elif contar_tempo(tempo_inicial) == 40 and contador == 2:
            for _ in range(4):
                grupo.add(Trofeu(mapa))
            return contador - 1
        elif contar_tempo(tempo_inicial) == 20 and contador == 1:
            for _ in range(4):
                grupo.add(Trofeu(mapa))
            return contador - 1
        else:
            return contador

