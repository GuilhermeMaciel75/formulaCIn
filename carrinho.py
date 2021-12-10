import pygame as pg
import os 

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
            self.carro = pg.image.load(os.path.join('imagens','carro_esquerda.png'))
            

        if tecla[self.direita]:

            self.x += self.velocidade 
            self.carro = pg.image.load(os.path.join('imagens','carro_direita.png'))


        if tecla[self.cima]:
            
            self.y -= self.velocidade
            self.carro = pg.image.load(os.path.join('imagens','carro_cima.png'))


        if tecla[self.baixo]:

            self.y += self.velocidade
            self.carro = pg.image.load(os.path.join('imagens','carro_baixo.png'))

        return tecla

    #Função responsável por escrever na tela 
    def escrtia(self):

        self.win.blit(self.carro, (self.x, self.y))
        pg.display.update()


def main():
    #Definindo o tamanho da tela
    screen = pg.display.set_mode((1080, 720))

    #Declarando a variável clock
    clock = pg.time.Clock()

    #Passando a imagem inical do carro
    carro = pg.image.load(os.path.join('imagens','carro_direita.png'))

    #Criando o objeto player
    player1 = Player(screen, 540, 360, pg.K_a, pg.K_d, pg.K_w, pg.K_s, carro)
    player2 = Player(screen, 540, 360, pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN, carro)

    #Variável responsável por deixar o loop infinito
    jogo_loop = True

    #Loop que roda até o jogo acabar
    while jogo_loop:
        #fps
        clock.tick(60)
        for event in pg.event.get():
            #caso queira sair do jogo
            if event.type == pg.QUIT:
                jogo_loop = False

            #chamando a função de movimento dos players
            player1.controle()
            player2.controle()

            screen.fill((40,40,40))

            #escrevendo na tela o movimento
            player1.escrtia()
            player2.escrtia()

            pg.display.flip()
            

#Chamando a função main
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    exit()
