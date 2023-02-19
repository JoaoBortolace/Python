from random import randint as rand

numAle = (rand(1, 10), rand(1, 10), rand(1, 10), rand(1, 10), rand(1, 10))

print('Os valores sorteados foram: ', end='')
for n in numAle:
    print(n, end=' ')

print(f'\nO maior valor sorteado foi {max(numAle)}')
print(f'O menor valor sorteado foi {min(numAle)}')
