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
        self.rotate = 0

        #Comandos de movimentação
        self.esquerda = esquerda
        self.direita = direita
        self.cima = cima
        self.baixo = baixo

        #comandos atributos do carro
        self.velocidade = 5
        self.image = carro
        self.image = pg.transform.scale(self.image, (70,50))
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        
        


    #Função responável por movimentar o carrinho na direção desejada
    def controle(self):

        tecla = pg.key.get_pressed()

        if tecla[self.esquerda]:   
            self.x -= self.velocidade
        

        if tecla[self.direita]:
            self.x += self.velocidade 



        if tecla[self.cima]:       
            self.y -= self.velocidade



        if tecla[self.baixo]:
            self.y += self.velocidade

    #Função responsável por escrever na tela 
    def escrita(self, sprites):

        self.rect = self.image.get_rect(center = (self.x, self.y))
        sprites.draw(self.win)
        pg.display.flip()
