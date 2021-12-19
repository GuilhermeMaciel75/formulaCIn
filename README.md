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
> Item é uma classe mãe que possui como variáveis a posição (que utiliza um método randomizar_posicao para preencher), altura, largura e o tipo do item, se é banana, raio ou troféu. Os métodos vinculados a classe são: randomizar_item(), que retorna uma string (banana ou raio), desenhar_item() que desenha na tela o sprite que é passado como parâmetro do método e o randomizar_posicao() que retorna uma lista contendo as coordenadas x e y do item.
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
> Em telas.py. Desenha a tela anterior à execução do jogo, que apresenta o nome do jogo e uma mensagem indicando como começar o jogo para o jogador, além de decorações na temática do game.
- **def tela_final()**:
> Em telas.py. Desenha a tela final após o cronômetro do jogo zerar, apresenta uma mensagem com o resultado da partida e indica ao jogador como reiniciar o jogo.
- **def  mostrar_pontuacao()**:
> Em pontuacao.py. Imprime na parte direita da tela a pontuação de cada jogador de acordo com seus respectivos desempenhos no jogo, além de imprimir imagens dos carros juntos das pontuações para melhor visualização.
- **def contar_tempo()**:
> Em cronometro.py. Contador utilizado para a obtenção do tempo de jogo atual e que retorna o tempo restante de corrida.
- **def mostra_tempo()**:
> Em cronometro.py. Utiliza a função contar_tempo e imprime na tela o tempo para que a corrida acabe.
- **def adicionar_powerups()**:
> Em adicionar_powerups.py. Função responsável por distribuir os itens na tela aleatoriamente no início do jogo. Distribui novamente itens aleatoriamente de acordo com o tempo, utilizando a função contar_tempo e um contador de coleta de itens.
- **def  reiniciar()**:
> Em reiniciar_atributos.py. Função responsável por reiniciar o jogo ao término dele, spawnando novamente os players nos seus respectivos lugares, zerando pontuações e realocando os itens coletáveis aleatoriamente.

## Bibliotecas/Módulos usada(o)s:
- **Pygame**:
> Esta biblioteca é um conjunto de módulos que foi desenvolvida para a escrita de jogos, ela permite que você crie jogos e programas multimidia a partir da linguagem python.
- **Random**:
> Este módulo implementa geradores de números pseudoaleatórios. Foi usado no jogo para o _spawn_ aleatorio de itens coletáveis.

## Conceitos:
- **Laços**:
> Um Laço é uma estrutura de repetição que permite a execução de um determinado comando diversas vezes seguidas, enquanto uma determinada condição é atendida. No projeto, utiliza-se laços para a atualização do jogo a cada frame, criando a possibilidade de ação do jogador, de spawn de itens e da contagem da pontuação.
- **Estruturas condicionais**:
> Uma estrutura condicional corresponde à uma função utilizada para determinar a veracidade de uma ou mais proposições, e a partir da resposta decidir qual bloco de códigos será execultado à seguir. No projeto, as principais utilizações de estruturas condicionais são determinar qual ação foi tomada pelo jogador, a partir de um input do teclado, determinar se um player coletou algum powerup ou algum troféu e determinar se um player está colidindo com a parede do mapa.
- **Funções**:
> Uma função é um bloco de códigos que executa algum comando predefinido quando chamada. No processo de sua definição os comandos são agrupados e à eles é dado um nome específico, pelo qual vai poder ser chamado. Funções são estruturas essenciais em um programa, pois evitam a repetição de um conjunto de comandos e auxiliam na modularização do código.
- **Classes e Objetos**:
> Quando um código é estruturado por meio da orientação à objetos, qualquer estrutura que deseja-se manipular e modificar durante o funcionamento do programa é um objeto. Já uma classe é uma estrutura responsável pela criação de cada objeto a ser utilizado no código. Toda vez que uma classe é instanciada, um novo objeto é criado de acordo com a definição de inicialização de sua respectiva classe. Em um programa, classes e objetos são essenciais para a organização do código, pois permitem a sua modularização.

## Desafios/Experiência:

- **Pygame**:
> A utilização obrigatória do Pygame foi um desafio, visto que os membros do grupo tinham pouca ou nenhuma familiaridade com ele. Aprendemos a utilizar suas funções de forma a conceber o sistema interativo que se deu no projeto, e combinados com os conhecimentos básicos de Python que aprendemos, conseguimos atingir os objetivos determinados.
- **Programação Orientada a Objetos**:
> A utilização de POO no projeto foi de extrema importância, proporcionando uma maior legibilidade e compactação do código. No grupo, tínhamos pessoas com experiência em POO e outra com nenhuma. A adaptação a esse estilo de programação resultou numa maior facilidade de trabalhar nesse projeto, visto que diversas vezes era necessário trabalhar com diversos atributos e funções que deveriam estar atrelados a uma mesma coisa, como por exemplo quando queremos trabalhar com o carro controlado pelo jogador e precisamos das coordenadas e dos comandos de movimento.
- **Github**:
> O uso do Github é fundamental na realização de projetos em grupo. Através dele, pudemos trabalhar em conjunto ao mesmo tempo que individualmente, com suas ferramentas a integridade funcional do projeto se manteve durante o período de realização. O aprendizado obtido será de extrema importância no âmbito que atuaremos.
-**Trabalho em equipe**:
> Tivemos uma dificuldade inicial em dividir as tarefas e em definir metas para os checkpoints, entretanto, com o tempo nos acertamos na organização e melhoramos o trabalho em equipe de forma a otimizar nosso tempo e produtividade. A divisão em 3 grupos (responsáveis por mapa, carro e itens) de duas pessoas contribuiu para que cada membro tivesse uma interação com um parceiro e uma divisão de trabalho equilibrada, além de incentivar uma competitividade amistosa entre grupos que implicou em uma maior agilidade no desenvolvimento. A experiência de programar em grupo foi positiva para todos os membros e consequentemente para a equipe.

#
###### *Projeto referente a matéria de Introdução a programação/CIN-UFPE no periodo de 2021.1. Começamos em 07/12/2021*
