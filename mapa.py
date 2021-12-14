import pygame as pg

# inicializando o PyGame
pg.init()


class Mapa():
    def __init__(self, x, y, window, mapa):
        # coordenadas do mapa
        self.x = x
        self.y = y

        # tela em que o mapa vai ser colocado
        self.win = window

        # matriz do mapa
        self.mapa = mapa


        # dicionario com as informaçoes de cada tile
        self.tiles = {
            0: {'sprite': pg.transform.scale(pg.image.load('assets/mapa/pista.png'), (18, 18)), 'type': 'chao'},
            1: {'sprite': pg.transform.scale(pg.image.load('assets/mapa/quadriculado_vermelho.png'), (18, 18)), 'type': 'parede'},
            2: {'sprite': pg.transform.scale(pg.image.load('assets/mapa/grama.png'), (18, 18))}, 'type': 'parede'}

    # Desenha o mapa
    def draw(self):
        # Caminha por todos os números da matriz e desenha a imagem correspondente nas cordenadas correspondentes
        for i in range(len(self.mapa[0])):
            for j in range(len(self.mapa)):
                self.win.blit(self.tiles[self.mapa[j][i]]['sprite'], (self.x + 18 * i, self.y + 18 * j))
