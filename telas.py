import pygame as pg
from pontuacao import mostrar_pontuacao

def tela_inicial(tela, x,y):
    tela.fill((0,0,0))
    fonte = pg.font.Font('assets/fontes/PressStart2P-Regular.ttf', 20)
    frase1 = fonte.render('FórmulaCIn', True, (255,255,255))
    frase2 = fonte.render('Pressione espaço para começar', True, (255,255,255))
    
    #tela.blit(pg.transform.scale(pg.image.load('assets/logo-cin.png'),(30,30)), (x+373,y-20))
    tela.blit(pg.transform.scale(pg.image.load('assets/bandeiras.png'),(250,250)), (x+275,y-175))
    tela.blit(frase1, (x+105,y+30))
    tela.blit(frase2, (150, 390))


def tela_final(screen, player1, player2):
    screen.fill((0, 0, 0))
    fonte = pg.font.Font('assets/fontes/PressStart2P-Regular.ttf', 20)
    resultado = fonte.render(f'Resultado', True, (255, 255, 255))
    screen.blit(resultado, (340, 100))
    mostrar_pontuacao(player1, player2, 350, 300, screen)
    texto = fonte.render(f'Pressione espaço para reiniciar', True, (255, 255, 255))
    screen.blit(texto, (135, 600))