# FormulaCIn
FormulaCIn é um jogo PvP baseado em uma experiência 2D de coleta de itens na pista e tem alguns itens que alteram a velocidade no mapa. Inicialmente, o jogador tem 60 segundos para coletar a maior quantidade de troféus que conseguir! Quem tiver a maior quantidade de troféus, ganha o game! Os outros itens dão os seguintes buffs/nerfs:
    
- Banana: Diminui a velocidade do player por 5 segundos
- Raio: Aumenta a velocidade do player por 5 segundos


## Equipe:

- Felipe Moraes (fbm3)
- Gabriel Henrique (ghv)
- Guilherme Maciel(gmm7)
- Gustavo Farias(gfn3)
- João Witor (jwtcs)
- Malu Melo (mvbm2)

## Link para o codigo fonte:
- https://github.com/malumelo7/formulaCIn

## Divisão de tarefas:

|      Equipes      |     Tarefas (principal)     |
| ------------------- | ------------------- |
|  **fbm3** e  **mvbm2**|  Criação dos itens e sistema de colisão com o carro |
|  **ghv** e **gmm7** |  Criação do Carro e sistema de colisão com a parede |
|  **gfn3** e **jwtcs** |  Criação do mapa, contador de pontuação e cronômetro |


## Organização do código:
O código foi estruturado Orientado à objetos e utilizou o recurso de loop para a lógica do jogo acontecer. As classes e funções importantes foram:

- **Carro()**:
>  Carro é uma classe responsável por armazenar todas propriedades e funções atreladas aos objetos controláveis do jogo. Nela armazenamos imagem, tamanho, posição na tela, velocidade de movimento, sprite, e as funções do carro que influenciam no andamento do jogo, como controle, pontuação, colisões e escrita na tela.
- **Item()**:
> Item é uma classe mãe que possui como variáveis a posição (que utiliza um método randomize_position para preencher), altura, largura e o tipo do item, se é banana, raio ou troféu. Os métodos vinculados a classe são: randomizar_item(), que retorna uma string (banana ou raio), desenhar_item() que desenha na tela o sprite que é passado como parâmetro do método e o randomize_position() que retorna uma lista contendo as coordenadas x e y do item.
- **Banana()**:
> A classe banana é uma subclasse da classe Item e ela contém o asset que representa o item banana, a definição de escala e o ponto de referência do item.
- **Raio()**:
> A classe raio é uma subclasse da classe Item e ela contém o asset que representa o item raio, a definição de escala e o ponto de referência do item.
- **Trofeu()**:
> A classe trofeu é uma subclasse da classe Item e ela contém o asset que representa o item troféu, a definição de escala e o ponto de referência do item. Além disso, a classe possui um método adicionar_trofeus() que adiciona no grupo de sprites para spawnar na tela.
- **Mapa()**:
> A classe mapa possui como variáveis a posição x e y do mapa (que é referenciado a partir do canto superior esquerdo), a janela que o mapa será renderizado e uma matriz(lista de listas) que representa qual o tipo de imagem que será renderizado no pixel para gerar o mapa.A classe mapa possui um método draw() que serve para renderizar na tela os pixels definidos pela matriz.
- **Grama(), Pista() e Quadriculado()**
> Essas classes são utilizadas para vincular o asset a cada uma delas, e utilizamos na classe mapa para criação.
- **def main()**:
> Função principal do jogo. É onde está o loop para que o jogo rode, recebemos os comandos de início, reinício e encerramento do jogo, aplicamos as funções para execução do jogo.
- **def tela_inicial()**:
> Em tela_inicial.py. Desenha a tela anterior à execução do jogo, que apresenta o nome do jogo e uma mensagem indicando como começar o jogo para o jogador, além de decorações na temática do game.
- **def  mostrar_pontuacao()**:
> Em pontuacao.py. Imprime na parte direita da tela a pontuação de cada jogador de acordo com seus respectivos desempenhos no jogo, além de imprimir imagens dos carros juntos das pontuações para melhor visualização.
- **def contar_tempo()**:
> Em cronometro.py. Contador utilizado para a obtenção do tempo de jogo atual e que retorna o tempo restante de corrida.
- **def mostra_tempo()**:
> Em cronometro.py. Utiliza a função contar_tempo e imprime na tela o tempo para que a corrida acabe.
- **def adicionar_powerups()**:
> Em adicionar_powerups.py. Função responsável por distribuir os itens na tela aleatoriamente no início do jogo. Distribui novamente itens aleatoriamente de acordo com o tempo, utilizando a função contar_tempo e um contador de coleta de itens.

## Bibliotecas/Módulos usada(o)s:
- **Pygame**:
> Esta biblioteca é um conjunto de módulos que foi desenvolvida para a escrita de jogos, ela permite que você crie jogos e programas multimidia a partir da linguagem python.
- **Random**:
> Este módulo implementa geradores de números pseudoaleatórios. Foi usado no jogo para o _spawn_ aleatorio de itens coletáveis.

## Conceitos:
- **Laços**:
> Xalala
- **Estruturas condicionais**:
> Xalala
- **Funções**:
> Xalala
- **Classes e Objetos**:
> Xalala

## Desafios/Experiência:

- **Xalala**:
> Xalala
- **Xalala**:
> Xalala
#
###### *Projeto referente a matéria de Introdução a programação/CIN-UFPE no periodo de 20201.1. Começamos em 07/12/2021*
