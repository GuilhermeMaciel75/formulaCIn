import pygame as pg
import os

from car import Player

def main():
    #Definindo o tamanho da tela
    screen = pg.display.set_mode((1080, 720))
    pg.display.set_caption("FormulaCIN")

    #Declarando a variável clock
    clock = pg.time.Clock()

    #Passando a imagem inical do carro
    carro = pg.image.load(os.path.join('assets','carro_direita.png'))

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