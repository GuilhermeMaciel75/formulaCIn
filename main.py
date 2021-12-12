import pygame as pg

from car import Player
from mapa import Mapa
from cronometro import mostrar_tempo


def main():
    #Definindo o tamanho da tela
    screen = pg.display.set_mode((900, 774))
    pg.display.set_caption("FormulaCIN")

    #Declarando a variável clock
    clock = pg.time.Clock()

    #Criando o Mapa
    mapa = Mapa(0, 0, screen, 'mapa1')

    #Passando a imagem inical do carro
    carro = pg.image.load('assets/carro_direita.png').convert_alpha()

    #Criando o objeto player
    player1 = Player(screen, 565, 360, pg.K_a, pg.K_d, pg.K_w, pg.K_s, carro)
    player2 = Player(screen, 80, 360, pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN, pg.transform.rotate(carro, 180))

    #Criando o grupo de sprites dos carros
    lista_sprites = pg.sprite.Group()
    lista_sprites.add(player1)
    lista_sprites.add(player2)

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
        pg.display.flip()
        
        #Desenhando o mapa
        screen.fill("Black")
        mapa.draw()

        #Startando o cronometro        
        if mostrar_tempo(690,30,screen) == 0:
            pass # aqui vai ser o que vai acontecer quando acabar o jogo
        
        #escrevendo na tela o movimento
        player1.escrita(lista_sprites)
        player2.escrita(lista_sprites)

                
#Chamando a função main
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    exit()