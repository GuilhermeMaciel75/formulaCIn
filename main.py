import pygame as pg
from pygame.constants import K_SPACE

from adicionar_powerups import adicionar_powerups
from carro import Carro, Carro2
from mapa import Mapa
from cronometro import contar_tempo, mostrar_tempo
from objects.item import Item
from objects.matriz_mapa import mapa1
from objects.trophy import Trophy
from pontuacao import mostrar_pontuacao
from telas import tela_inicial
from telas import tela_final


def main():
    #Declarando a variável clock
    clock = pg.time.Clock()
    
    clock.tick(60)
    #Adicionando a música e colocando ela para tocar
    pg.mixer.music.set_volume(0.2)
    som = pg.mixer.music.load('assets/efeitos_sonoros/TopGear.mp3')
    pg.mixer.music.play(-1)

    #Definindo o tamanho da tela
    screen = pg.display.set_mode((900, 774))
    pg.display.set_caption("FormulaCIN") # titulo do jogo
    pg.display.set_icon(pg.image.load('assets/logo-cin.png')) # icone do jogo
    
    
    jogo_loop = False
    tempo_esgotado = False
    #loop que vai dar na tela inicial, esperando o jogador apertar 'espaço' para começar o jogo
    while jogo_loop is False:
        tela_inicial(screen, 150, 200)
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        
        tecla = pg.key.get_pressed()
        if tecla[K_SPACE]: 
            jogo_loop = True
            tempo_inicial = int(pg.time.get_ticks() / 1000)
    
    #Criando o Mapa
    grupo_parede = pg.sprite.Group()
    
    mapa = Mapa(0, 0, screen, mapa1, grupo_parede)
    grupo_parede.draw(screen)   
    mapa.draw()
    
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
    
    contador_trofeus = 3
    contador_tempo_itens = 3
    contador_itens = 0
    
    while jogo_loop:
        
        contador_tempo_itens = adicionar_powerups(grupo_banana, grupo_raio, contador_tempo_itens, mapa, tempo_inicial)
        contador_trofeus = Trophy.adicionar_trofeu(grupo_trofeu, contador_trofeus, mapa, tempo_inicial)
        

        #fps
        clock.tick(60)
        for event in pg.event.get():
            #caso queira sair do jogo
            if event.type == pg.QUIT:
                jogo_loop = False

        #se o tempo acabar
        if contar_tempo(tempo_inicial) == 0:
            tempo_esgotado = True
            tela_final(screen, player1, player2)
            pg.display.flip()

            # se apertar espaço
            tecla = pg.key.get_pressed()
            if tecla[K_SPACE]:
                tempo_esgotado = False
                tempo_inicial = int(pg.time.get_ticks() / 1000)  # reiniciando o cronometro
                # reiniciar o mapa (tirar os itens)
                # reiniciar a posição dos carrinhos

        if not tempo_esgotado:

            #chamando a função de movimento dos players
            player1.controle()
            player2.controle()
            pg.display.flip()
        
            #Verificando colisão
            player1.update_colisao(grupo_trofeu, grupo_banana, grupo_raio, grupo_parede, player1, tempo_inicial)
            player2.update_colisao(grupo_trofeu, grupo_banana, grupo_raio, grupo_parede, player2, tempo_inicial)

            #Desenhando o mapa e os itens

            screen.blit(pg.transform.scale(pg.image.load('assets/mapa/fundo.png'),(900,774)), (0,0))

            Item.desenhar_item(grupo_banana, screen)
            Item.desenhar_item(grupo_raio, screen)
            Item.desenhar_item(grupo_trofeu, screen)

            #Startando o cronometro
            mostrar_tempo(690,30,screen, tempo_inicial)
        
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