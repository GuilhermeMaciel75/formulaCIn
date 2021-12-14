import pygame as pg
from pygame import transform
from pygame import sprite

from car import Player
from mapa import Mapa
from cronometro import mostrar_tempo
from objects.item import Item
from objects.item import Trophy


def main():
    #Definindo o tamanho da tela
    screen = pg.display.set_mode((900, 774))
    pg.display.set_caption("FormulaCIN")

    #Declarando a variável clock
    clock = pg.time.Clock()

    #Criando o Mapa
    mapa = Mapa(0, 0, screen, 'mapa1')

    #Passando a imagem inical do carro
    carro = pg.image.load('assets/carro_esquerda.png').convert_alpha()

    #Criando o objeto player
    player1 = Player(screen, 600, 360, pg.K_a, pg.K_d, pg.K_w, pg.K_s, carro)
    player2 = Player(screen, 90, 360, pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN, pg.transform.rotate(carro, 180))

    #Criando o grupo de sprites dos carros
    lista_sprites = pg.sprite.Group()
    lista_sprites.add(player1)
    lista_sprites.add(player2)

    #Criando grupo dos powerups e do troféu
    grupo_banana = pg.sprite.Group()
    grupo_raio = pg.sprite.Group()
    grupo_trofeu = pg.sprite.Group()

    #Variável responsável por deixar o loop infinito
    jogo_loop = True


    #Loop que roda até o jogo acabar
    contador_trofeus = 3
    contador_itens = 3
    while jogo_loop:

        contador_itens = Item.adicionar_powerups(grupo_banana, grupo_raio, contador_itens)
        contador_trofeus = Trophy.adicionar_trofeu(grupo_trofeu, contador_trofeus)


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
        
        #Verificando colisão
        player1.update_colisao(grupo_trofeu, grupo_banana, grupo_raio, player1)
        player2.update_colisao(grupo_trofeu, grupo_banana, grupo_raio, player2)

        #Desenhando o mapa e os itens
        screen.fill("Black")
        mapa.draw()
        Item.desenhar_powerups(grupo_banana, screen)
        Item.desenhar_powerups(grupo_raio, screen)
        Trophy.desenhar_trofeu(grupo_trofeu, screen)

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