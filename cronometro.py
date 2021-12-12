import pygame as pg

pg.init()

def contar_tempo():
    tempo_atual = int(pg.time.get_ticks() / 1000)
    tempo_restante = 60 - tempo_atual

    return tempo_restante

def mostrar_tempo(x, y, screen):
    fonte = pg.font.Font('assets/fontes/PressStart2P-Regular.ttf', 20)

    tempo = fonte.render(f'Tempo:{contar_tempo()}', True, (255,255,255))    
    
    screen.blit(tempo, (x,y))
         