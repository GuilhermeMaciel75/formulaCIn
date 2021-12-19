import pygame as pg
from carro import Carro, Carro2

SPWAN_PLAYER1_X = 558
SPWAN_PLAYER_Y = 343
SPWAN_PLAYER2_X = 60
VELOCIDADE = 3

def reiniciar(player1, player2, grupo_banana, grupo_raio, grupo_trofeu):
    
    pg.sprite.Group.empty(grupo_banana)
    pg.sprite.Group.empty(grupo_raio)
    pg.sprite.Group.empty(grupo_trofeu)

    # Reiniciar a posição dos carrinhos
    player1.set_posicao_x = SPWAN_PLAYER1_X
    player1.set_posicao_y = SPWAN_PLAYER_Y
    player1.set_direcao = 0

    player2.set_posicao_x = SPWAN_PLAYER2_X
    player2.set_posicao_y = SPWAN_PLAYER_Y
    player2.set_direcao = 1

    # Reiniciar a contagem da pontuação dos carrinhos
    player1.set_pontuacao = 0
    player2.set_pontuacao = 0

    player1.set_velocidade = VELOCIDADE
    player2.set_velocidade = VELOCIDADE