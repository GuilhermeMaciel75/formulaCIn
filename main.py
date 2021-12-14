import pygame as pg

from adicionar_powerups import adicionar_powerups
from carro import Carro, Carro2
from mapa import Mapa
from cronometro import mostrar_tempo
from objects.item import Item
from objects.matriz_mapa import mapa1
from objects.trophy import Trophy
from pontuacao import mostrar_pontuacao


def main():
    
    #Adicionando a música e colocando ela para tocart
    pg.mixer.music.set_volume(0.2)
    som = pg.mixer.music.load('assets/efeitos_sonoros/TopGear.mp3')
    pg.mixer.music.play(-1)

    #Definindo o tamanho da tela
    screen = pg.display.set_mode((900, 774))
    pg.display.set_caption("FormulaCIN")

    #Declarando a variável clock
    clock = pg.time.Clock()

    #Criando o Mapa
    mapa = Mapa(0, 0, screen, mapa1)

    #Criando o objeto player
    player1 = Carro(screen, 600, 360, pg.K_a, pg.K_d, pg.K_w, pg.K_s, "Player 1")
    player2 = Carro2(screen, 90, 360, pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN, "Player 2")

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

        contador_itens = adicionar_powerups(grupo_banana, grupo_raio, contador_itens)
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
        Item.desenhar_item(grupo_banana, screen)
        Item.desenhar_item(grupo_raio, screen)
        Item.desenhar_item(grupo_trofeu, screen)

        #Startando o cronometro        
        if mostrar_tempo(690,30,screen) == 0:
            pass # aqui vai ser o que vai acontecer quando acabar o jogo
        
        #Mostrando pontuação
        mostrar_pontuacao(player1, player2, 690, 300, screen)

        #escrevendo na tela o movimento
        player1.escrita(lista_sprites)
        player2.escrita(lista_sprites)

                
#Chamando a função main
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    exit()