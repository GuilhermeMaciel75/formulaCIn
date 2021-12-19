import pygame as pg

SPAWN_PLAYER1_X = 558
SPAWN_PLAYER_Y = 343
SPAWN_PLAYER2_X = 60
VELOCIDADE = 3

# Função responsável pelo reinício do jogo
def reiniciar(player1, player2, grupo_banana, grupo_raio, grupo_trofeu):
    # Reiniciar os itens dos seus respectivos grupos
    pg.sprite.Group.empty(grupo_banana)
    pg.sprite.Group.empty(grupo_raio)
    pg.sprite.Group.empty(grupo_trofeu)

    # Reiniciar a posição dos carrinhos
    player1.set_posicao_x = SPAWN_PLAYER1_X
    player1.set_posicao_y = SPAWN_PLAYER_Y
    player1.set_direcao = 0

    player2.set_posicao_x = SPAWN_PLAYER2_X
    player2.set_posicao_y = SPAWN_PLAYER_Y
    player2.set_direcao = 1

    # Reiniciar a contagem da pontuação dos carrinhos
    player1.set_pontuacao = 0
    player2.set_pontuacao = 0

    # Reiniciar a velocidade dos carrinhos
    player1.set_velocidade = VELOCIDADE
    player2.set_velocidade = VELOCIDADE