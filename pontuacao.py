import pygame as pg

from carro import Carro
from objects.trophy import Trophy

def mostrar_pontuacao(player1: Carro, player2: Carro, x, y, screen):
    fonte = pg.font.Font('assets/fontes/PressStart2P-Regular.ttf', 20)
    nome_player1 = fonte.render(f'{player1.get_nome}', True, (255,255,255))
    pontuacao_player1 = fonte.render(f'{player1.get_pontuacao}', True, (255,255,255))
    nome_player2 = fonte.render(f'{player2.get_nome}', True, (255,255,255))
    pontuacao_player2 = fonte.render(f'{player2.get_pontuacao}', True, (255,255,255))

    image = pg.image.load('assets/trofeu.png').convert_alpha()
    image = pg.transform.scale(image, (20, 20))

    screen.blit(nome_player1, (x, y))
    screen.blit(pontuacao_player1, (x + 40, y + 30))
    screen.blit(image, (x + 80, y + 30))

    screen.blit(nome_player2, (x, y + 90))
    screen.blit(pontuacao_player2, (x + 40, y + 120))
    screen.blit(image, (x + 80, y + 120))
