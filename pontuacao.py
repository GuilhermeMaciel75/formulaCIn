import pygame as pg
from carro import Carro, Carro2

def mostrar_pontuacao(player1: Carro, player2: Carro2, x, y, screen):
    # Criar o placar de pontuação dos players
    fonte = pg.font.Font('assets/fontes/PressStart2P-Regular.ttf', 20)
    nome_player1 = fonte.render('Player', True, (255,255,255))
    pontuacao_player1 = fonte.render(f'{player1.get_pontuacao}', True, (255,255,255))
    nome_player2 = fonte.render('Player', True, (255,255,255))
    pontuacao_player2 = fonte.render(f'{player2.get_pontuacao}', True, (255,255,255))

    imagem_trofeu = pg.image.load('assets/trofeu.png').convert_alpha()
    imagem_trofeu = pg.transform.scale(imagem_trofeu, (20, 20))

    # Criar os carrinhos que representam cada player
    imagem_carrinho1 = pg.image.load('assets/carro_azul.png')
    imagem_carrinho1 = pg.transform.scale(imagem_carrinho1, (48,36))
    imagem_carrinho1 = pg.transform.rotate(imagem_carrinho1, -90)
    imagem_carrinho2 = pg.image.load('assets/carro_vermelho.png')
    imagem_carrinho2 = pg.transform.scale(imagem_carrinho2, (48,36))
    imagem_carrinho2 = pg.transform.rotate(imagem_carrinho2, 90)

    # Desenhar a pontuação do player 1
    screen.blit(nome_player1, (x, y - 10))
    screen.blit(pontuacao_player1, (x + 40, y + 20))
    screen.blit(imagem_trofeu, (x + 80, y + 20))
    screen.blit(imagem_carrinho1, (x + 130, y - 10))

    # Desenhar a pontuação do player 2
    screen.blit(nome_player2, (x, y + 100))
    screen.blit(pontuacao_player2, (x + 40, y + 130))
    screen.blit(imagem_trofeu, (x + 80, y + 130))
    screen.blit(imagem_carrinho2, (x + 130, y + 100))