''' Em uma cidade se deseja sincronizar os semáforos. Com isto, quando um semáforo abre (fica verde), os veículos que nele estavam parados tendem a encontrar os próximos semáforos também abertos. Para que isto seja feito, os próximos semáforos precisam abrir um pouco depois, dependendo da velocidade permitida na via e da distância entre eles. Assim, ao abrir o semáforo, um veículo começa a acelerar até atingir a velocidade permitida, que mantém até chegar ao próximo semáforo, levando um certo tempo para percorrer essa distância. Para que encontre o próximo semáforo aberto, este deve abrir um pouco antes da chegada do veículo (por ex: 3 segundos antes). Faça assim um algoritmo que informe quanto tempo depois um semáforo deve abrir, dada as seguintes informações: 
a. a distância desde o semáforo anterior 
b. a velocidade permitida da via 
c. a aceleração típica dos carros '''

# pedir distancia entre os semáforos 
# velocidade máxima da via
# aceleração típica dos carros
# calcular o tempo que o carro leva para atingir a velocidade máxima
# descobrir a distância percorrida durante a aceleração
# comparar a distância percorrida durante a aceleração com a distância entre os semáforos 
# se o carro conseguiu atingir a velocidade máxima: 
''' - calcula o tempo da aceleração 
    - calcula a distância percorrida acelerando 
    - calcula a distância restante 
    - calcula o tempo da parte restante em velocidade constante
    - soma os tempos'''
# se o carro não conseguiu atingir a velocidade máxima:
''' calcula o tempo total (tempo de aceleração + tempo restante)  '''
# descobrir quando o proximo semáforo deve abrir (tempo total - 3 segundos)
# resultado: tempo total de chegada, tempo ideal de abertura do proximo semáforo

import math

distancia_semaforos = float(input("Digite a distância entre os semáforos (em metros):"))
velocidade_maxima = float(input("Digite a velocidade máxima da via (em m/s):"))
aceleracao = float(input("Digite a aceleração típica dos carros (em m/s²):"))

tempo_aceleracao = velocidade_maxima / aceleracao
distancia_percorrida = aceleracao * tempo_aceleracao**2 /  2

if distancia_percorrida <= distancia_semaforos:
    distancia_restante = distancia_semaforos - distancia_percorrida
    tempo_velocidade_constante = distancia_restante / velocidade_maxima
    tempo_total =  tempo_aceleracao + tempo_velocidade_constante

else:
    tempo_total2 = math.sqrt(2 * distancia_semaforos / aceleracao)