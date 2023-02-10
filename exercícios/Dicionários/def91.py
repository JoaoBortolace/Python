from random import randint as random
from time import sleep as delay

print('Valores sorteados: ')
jogadores = {}
for j in range(1, 5):
    jogadores[f'jogador{j}'] = random(1, 6)
for k, v in jogadores.items():
    print(f'\tO {k} tirou {v}')
    delay(1)
# Ordenado o dicinário em ordem decrescente
dicAux = {}  # Dicionário auxiliar
# Os elementos do dicionário serão passados em ordem decrescente para dicionário auxiliar
while len(dicAux) < 4:  # O laço é repetido enquanto todos os valores não foram passados
    maiorValor = max(jogadores.values())  # Busca qual foi o maior valor do dado tirado
    maior = ''  # Salva a key do maior valor
    for k, v in jogadores.items():  # Este laço busca a key do maior valor de dado encontrado
        if v == maiorValor:
            maior = k
            break
    dicAux[maior] = jogadores[maior]  # Salva o maior elemento no dicionário auxiliar
    del jogadores[maior]  # Apaga este maior elemento do dicionário pricinpal
    # Como o maior é apagado, na próxima iteração o maior será o segundo maior do total, e depois terceiro...

jogadores = dicAux.copy()  # Passa os dados já ordenados do dicionário auxiliar para o principal
del dicAux  # Apaga o auxiliar
print('Raking dos jogadores')
c = 1
for k, v in jogadores.items():
    print(f'\t{c}º lugar: {k} com {v}')
    c += 1
    delay(1)
