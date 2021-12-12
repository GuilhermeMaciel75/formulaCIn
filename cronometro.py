import pygame as pg

pg.init()

def mostrar_tempo(x, y, screen):
    fonte = pg.font.Font('assets/fontes/PressStart2P-Regular.ttf', 20)
    tempo_atual = int(pg.time.get_ticks() / 1000)
    
    tempo_restante = 60 - tempo_atual
    tempo = fonte.render(f'Tempo:{tempo_restante}', True, (255,255,255))    
    
    screen.blit(tempo, (x,y))
    return tempo_restante
         