import pygame as pg
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
        self.velocidade = 2
        self.image = pg.image.load('assets/carro_azul.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (40,30))
        self.rect = self.image.get_rect(midright = (self.x, self.y))
        self.pontuacao = 0
        self.nome = nome

        self.sprites = []
        self.sprites.append(self.image)
        self.sprites.append(pg.transform.rotate(self.image,180))
        self.sprites.append(pg.transform.rotate(self.image,90))
        self.sprites.append(pg.transform.rotate(self.image,270))

    #Getters
    @property
    def get_pontuacao(self):
        return self.pontuacao
        
    @property
    def get_nome(self):
        return self.nome
        
    #Função responável por movimentar o carrinho na direção desejada
    def controle(self):

        tecla = pg.key.get_pressed()

        if tecla[self.esquerda]: 

            self.image = pg.transform.scale(self.sprites[0], (40,30))
            self.x -= self.velocidade

        if tecla[self.direita]:

            self.image = pg.transform.scale(self.sprites[1], (40,30))
            self.x += self.velocidade 

        if tecla[self.cima]:     
            
            self.image = pg.transform.scale(self.sprites[3], (30,40))
            self.y -= self.velocidade

        if tecla[self.baixo]:

            self.image = pg.transform.scale(self.sprites[2], (30,40))
            self.y += self.velocidade

    #Função responsável por escrever na tela 
    def escrita(self, sprites):

        self.rect = self.image.get_rect(midright = (self.x, self.y))
        sprites.draw(self.win)
    
        pg.display.flip()

    def colisao_trofeu(self, grupo_trofeu, player):

        if pg.sprite.spritecollide(player, grupo_trofeu, True):

            self.pontuacao += 1
            print(f"{self.get_nome} - Pontuação: {self.pontuacao}")
            
            #Efeito sonoro da coleta
            som = pg.mixer.Sound('assets/efeitos_sonoros/coleta_item.wav')
            pg.mixer.Sound.set_volume(som, 0.15)
            som.play()

            return self.pontuacao

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

    def update_colisao(self, trofeu, banana, raio, player):
        
        if self.colisao_banana(banana, player):
            #Definindo a velocidade e o tempo do buffer
            self.velocidade = 1
            self.final = contar_tempo() - 5

        if self.colisao_raio(raio, player):
            #Definindo a velocidade e o tempo do buffer
            self.velocidade = 5
            self.final = contar_tempo() - 5

        self.colisao_trofeu(trofeu, player)

        #Verifica se já deu o tempo do buffer
        self.tempo_atual = contar_tempo()
        if self.final > self.tempo_atual:
            self.velocidade = 2

#Classe para o carro2
class Carro2(Carro):
    def __init__(self, win, x, y, esquerda, direita, cima, baixo, nome):
        super().__init__(win, x, y, esquerda, direita, cima, baixo, nome)
        
        #Pegando a imagem
        self.image = pg.image.load('assets/carro_vermelho.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (40,30))
        
        #Transformando para sprite
        self.sprites = []
        self.sprites.append(pg.transform.rotate(self.image,180))
        self.sprites.append(self.image)
        self.sprites.append(pg.transform.rotate(self.image,270))
        self.sprites.append(pg.transform.rotate(self.image,90))