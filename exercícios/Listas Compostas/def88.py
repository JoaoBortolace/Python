from random import randint as random
from time import sleep as delay

print('-' * 35)
print(f"{'JOGA NA MEGA SENA':>26}")
print('-' * 35)
numJogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 4, f'SORTEANDO {numJogos} JOGOS', '-=' * 4)
jogos = []
for n in range(0, numJogos):
    jogo = []
    while len(jogo) < 6:
        numRandom = random(1, 60)
        if numRandom not in jogo:
            jogo.append(numRandom)
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    print(f'Jogo {n+1}: {jogos[n]}')
    delay(0.75)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
