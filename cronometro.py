import pygame as pg

def contar_tempo(tempo_inicial):
    tempo_atual = int(pg.time.get_ticks() / 1000)
    tempo_restante = 60 - tempo_atual + tempo_inicial

    if tempo_restante < 0:
        tempo_restante = 0

    return tempo_restante

def mostrar_tempo(x, y, screen, tempo_inicial):
    fonte = pg.font.Font('assets/fontes/PressStart2P-Regular.ttf', 20)

    tempo = fonte.render(f'Tempo:{contar_tempo(tempo_inicial)}', True, (255,255,255))    
    
    screen.blit(tempo, (x,y))
         