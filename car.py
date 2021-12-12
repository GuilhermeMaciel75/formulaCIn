import pygame as pg
from pygame.display import flip

#Classe responsável pelo moviemnto do player
class Player(pg.sprite.Sprite):

    def __init__(self, win, x, y, esquerda, direita, cima, baixo, carro):

        super().__init__()

        #Comandos de dimensão da tela e de colocação do player
        self.win = win
        self.x = x
        self.y = y

        #Comandos de movimentação
        self.esquerda = esquerda
        self.direita = direita
        self.cima = cima
        self.baixo = baixo

        #comandos atributos do carro
        self.velocidade = 2
        self.image = carro
        self.image = pg.transform.scale(self.image, (40,30))
        self.rect = self.image.get_rect(midright = (self.x, self.y))

        self.sprites = []
        self.sprites.append(self.image)
        self.sprites.append(pg.image.load('assets/carro_direita.png').convert_alpha())
        self.sprites.append(pg.image.load('assets/carro_cima.png').convert_alpha())
        self.sprites.append(pg.image.load('assets/carro_baixo.png').convert_alpha())
        
        
    #Função responável por movimentar o carrinho na direção desejada
    def controle(self):

        tecla = pg.key.get_pressed()

        if tecla[self.esquerda]: 
            self.image = pg.transform.scale(self.sprites[0], (40,30))
            self.x -= self.velocidade

        if tecla[self.direita]:
            self.image = pg.transform.scale(self.sprites[1], (40,30))
            self.x += self.velocidade 

        if tecla[self.cima]:     
            self.image = pg.transform.scale(self.sprites[2], (30,40))
            self.y -= self.velocidade

        if tecla[self.baixo]:
            self.image = pg.transform.scale(self.sprites[3], (30,40))
            self.y += self.velocidade

        return tecla

    #Função responsável por escrever na tela 
    def escrita(self, sprites):

        self.rect = self.image.get_rect(midright = (self.x, self.y))
        sprites.draw(self.win)
    
        pg.display.flip()


