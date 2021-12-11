import pygame as pg

#Classe responsável pelo moviemnto do player
class Player():

    #Função cosntrutuora das características 
    def __init__(self, win, x, y, esquerda, direita, cima, baixo, carro):

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
        self.velocidade = 10
        self.carro = carro


    #Função responável por movimentar o carrinho na direção desejada
    def controle(self):

        tecla = pg.key.get_pressed()

        if tecla[self.esquerda]:
            
            self.x -= self.velocidade
            self.carro = pg.image.load('assets/carro_esquerda.png')
            self.rect = self.carro.get_rect(center = (self.x, self.y))
            

        if tecla[self.direita]:

            self.x += self.velocidade 
            self.carro = pg.image.load('assets/carro_direita.png')


        if tecla[self.cima]:
            
            self.y -= self.velocidade
            self.carro = pg.image.load('assets/carro_cima.png')


        if tecla[self.baixo]:

            self.y += self.velocidade
            self.carro = pg.image.load('assets/carro_baixo.png')

        return tecla

    #Função responsável por escrever na tela 
    def escrita(self):

        self.win.blit(self.carro, (self.x, self.y))
        pg.display.update()
