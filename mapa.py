import pygame as pg
from objects.grama import Grama

from objects.pista import Pista
from objects.quadriculado import Quadriculado

# inicializando o PyGame
pg.init()


class Mapa():
    def __init__(self, x, y, window, mapa, grupo_parede):
        # coordenadas do mapa
        self.x = x
        self.y = y

        # tela em que o mapa vai ser colocado
        self.win = window

        # matriz do mapa
        self.mapa = mapa

        
        self.grupo_parede = grupo_parede

    # Desenha o mapa
    def draw(self):
        # Caminha por todos os números da matriz e desenha a imagem correspondente nas cordenadas correspondentes
        for i in range(len(self.mapa[0])):
            for j in range(len(self.mapa)):
                
                
                if self.mapa[j][i] == 1:
                    self.grupo_parede.add(Quadriculado(self.x + 18 * i, self.y + 18 * j))

                elif self.mapa[j][i] == 2:
                    self.grupo_parede.add(Grama(self.x + 18 * i, self.y + 18 * j))
                
        self.grupo_parede.draw(self.win)
        #self.grupo_pista.draw(self.win)
        