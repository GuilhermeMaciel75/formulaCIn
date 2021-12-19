from cronometro import contar_tempo
from objects.banana import Banana
from objects.item import Item
from objects.raio import Raio

# Função responsável criar os sprites dos powerups e por adicioná-los à seus respectivos grupos
def adicionar_powerups(grupo_banana, grupo_raio, contador, mapa, tempo_inicial):

    # Criar powerups quando o jogo for iniciado
    if contar_tempo(tempo_inicial) == 60 and contador == 3:
        for _ in range(3):
            if Item.randomizar_item() == "banana":
                grupo_banana.add(Banana(mapa))
            else:
                grupo_raio.add(Raio(mapa))
        return contador - 1

    # Criar powerups quando o tempo restante for 40 segundos
    elif contar_tempo(tempo_inicial) == 40 and contador == 2:
        if Item.randomizar_item() == "banana":
            grupo_banana.add(Banana(mapa))
        else:
            grupo_raio.add(Raio(mapa))
        return contador - 1

    # Criar powerups quando o tempo restante for 20 segundos
    elif contar_tempo(tempo_inicial) == 20 and contador == 1:
        if Item.randomizar_item() == "banana":
            grupo_banana.add(Banana(mapa))
        else:
            grupo_raio.add(Raio(mapa))
        return contador - 1
        
    else:
        return contador
