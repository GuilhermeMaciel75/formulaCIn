from typing import Tuple
import pygame as pg
from pygame import Surface, surface
from pygame import sprite
from cronometro import contar_tempo

#Classe responsável pelo moviemnto do player
class Carro(pg.sprite.Sprite):

    def __init__(self, win, x, y, esquerda, direita, cima, baixo, nome):

        super().__init__()

        #Comandos de dimensão da tela e de colocação do player
        self.win = win
        self.x = x
        self.y = y
        self.tempo_atual = 0
        self.final = 0

        #Comandos de movimentação
        self.esquerda = esquerda
        self.direita = direita
        self.cima = cima
        self.baixo = baixo

        #comandos atributos do carro
        self.velocidade = 3
        self.image = pg.image.load('assets/carro_azul.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (31,31))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self._pontuacao = 0
        self.nome = nome

        self.sprites = []
        self.sprites.append(self.image)
        self.sprites.append(pg.transform.rotate(self.image,180))
        self.sprites.append(pg.transform.rotate(self.image,90))
        self.sprites.append(pg.transform.rotate(self.image,270))

    #Getters
    @property
    def get_pontuacao(self):
        return self._pontuacao
        
    @property
    def get_nome(self):
        return self.nome

    @property
    def get_posicao_x(self):
        return self.rect.x

    @property
    def get_posicao_y(self):
        return self.rect.y

    @property
    def get_imagem(self):
        return self.image

    @property
    def get_velocidade(self):
        return self.velocidade
    #Setters
    @get_pontuacao.setter
    def set_pontuacao(self, value):
        self._pontuacao = value

    @get_posicao_x.setter
    def set_posicao_x(self, value):
        self.rect.x = value

    @get_posicao_y.setter
    def set_posicao_y(self, value):
        self.rect.y = value

    @get_imagem.setter
    def set_direcao(self, value):
        self.image = self.sprites[value]

    @get_velocidade.setter
    def set_velocidade(self, value):
        self.velocidade = value

    #Função responável por movimentar o carrinho na direção desejada
    def controle(self, grupo_parede):

        tecla = pg.key.get_pressed()

        if tecla[self.esquerda]: 

            self.rect.x -= self.velocidade
            lista_colidiu = pg.sprite.spritecollide(self, grupo_parede, False)
            
            for colidiu in lista_colidiu:
                self.rect.left = colidiu.rect.right
            
            self.image = pg.transform.scale(self.sprites[0], (31,31))

            

        if tecla[self.direita]:

            self.rect.x += self.velocidade 
            lista_colidiu = pg.sprite.spritecollide(self, grupo_parede, False)

            for colidiu in lista_colidiu:
                self.rect.right = colidiu.rect.left
            
            self.image = pg.transform.scale(self.sprites[1], (31,31))
            

        if tecla[self.cima]:     
            
            
            self.rect.y -= self.velocidade
            lista_colidiu = pg.sprite.spritecollide(self, grupo_parede, False)
            
            for colidiu in lista_colidiu:
                self.rect.top = colidiu.rect.bottom
            
            self.image = pg.transform.scale(self.sprites[3], (31,31))
            

        if tecla[self.baixo]:

            self.rect.y += self.velocidade
            lista_colidiu = pg.sprite.spritecollide(self, grupo_parede, False)
            
            for colidiu in lista_colidiu:
                
                self.rect.bottom = colidiu.rect.top

            self.image = pg.transform.scale(self.sprites[2], (31,31))
            

    #Função responsável por escrever na tela 
    def escrita(self, sprites):

        
        sprites.draw(self.win)
    
        pg.display.flip()

    def colisao_trofeu(self, grupo_trofeu, player):

        if pg.sprite.spritecollide(player, grupo_trofeu, True):

            self._pontuacao += 1
            print(f"{self.get_nome} - Pontuação: {self._pontuacao}")
            
            #Efeito sonoro da coleta
            som = pg.mixer.Sound('assets/efeitos_sonoros/coleta_item.wav')
            pg.mixer.Sound.set_volume(som, 0.15)
            som.play()

            return self._pontuacao

    def colisao_banana(self, grupo_banana, player):

        if pg.sprite.spritecollide(player, grupo_banana, True):

            print(f"{self.get_nome} - Banana")
            
            #Efeito sonoro da banana
            som = pg.mixer.Sound('assets/efeitos_sonoros/banana.wav')
            pg.mixer.Sound.set_volume(som, 0.15)
            som.play()

            return True

    def colisao_raio(self, grupo_raio, player):

        if pg.sprite.spritecollide(player, grupo_raio, True): 

            print(f"{self.get_nome} - Raio")
            
            #Efeito sonoro do raio
            som = pg.mixer.Sound('assets/efeitos_sonoros/raio.wav')
            pg.mixer.Sound.set_volume(som, 0.3)
            som.play()

            return True

    def colisao_parede(self, grupo_parede, player):

        pg.sprite.spritecollide(player, grupo_parede, False)

            #print('Bateu na parede')
        
    def update_colisao(self, trofeu, banana, raio, parede, player, tempo_inicial):
        
        if self.colisao_banana(banana, player):
            
            #Definindo a velocidade e o tempo do buffer
            self.velocidade = 1
            self.final = contar_tempo(tempo_inicial) - 5

        if self.colisao_raio(raio, player):

            #Definindo a velocidade e o tempo do buffer
            self.velocidade = 5
            self.final = contar_tempo(tempo_inicial) - 5

        self.colisao_trofeu(trofeu, player)

        #Verifica se já deu o tempo do buffer
        self.tempo_atual = contar_tempo(tempo_inicial)
        if self.final > self.tempo_atual:
            self.velocidade = 3

        self.colisao_parede(parede, player)

#Classe para o carro2
class Carro2(Carro):
    def __init__(self, win, x, y, esquerda, direita, cima, baixo, nome):
        super().__init__(win, x, y, esquerda, direita, cima, baixo, nome)
        
        #Pegando a imagem
        self.image = pg.image.load('assets/carro_vermelho.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (31,31))
        
        #Transformando para sprite
        self.sprites = []
        self.sprites.append(pg.transform.rotate(self.image,180))
        self.sprites.append(self.image)
        self.sprites.append(pg.transform.rotate(self.image,270))
        self.sprites.append(pg.transform.rotate(self.image,90))