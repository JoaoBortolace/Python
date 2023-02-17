# Funções auxiliares external
from random import randint as random
from time import sleep as delay


# Funções auxiliares próprias
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        delay(0.3)
        num_ram = random(1, 10)
        print(num_ram, end=' ', flush=True)
        lista.append(num_ram)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista}, temos {soma}')


# Programa Principal
numeros = []
sorteia(numeros)
somapar(numeros)
