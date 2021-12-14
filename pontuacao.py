import pygame as pg

from carro import Carro

def mostrar_pontuacao(player1: Carro, player2: Carro, x, y, screen):
    fonte = pg.font.Font('assets/fontes/PressStart2P-Regular.ttf', 20)
    pontuacao_player1 = fonte.render(f'{player1.get_nome}:{player1.get_pontuacao}', True, (255,255,255))
    pontuacao_player2 = fonte.render(f'{player2.get_nome}:{player2.get_pontuacao}', True, (255,255,255))

    screen.blit(pontuacao_player1, (x, y))
    screen.blit(pontuacao_player2, (x, y + 50))