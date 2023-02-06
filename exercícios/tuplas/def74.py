from random import randint as rand

numAle = (rand(0, 9), rand(0, 9), rand(0, 9), rand(0, 9), rand(0, 9))

print(f'Os valores sorteados foram: {numAle[0]} {numAle[1]} {numAle[2]} {numAle[3]} {numAle[4]}')
print(f'O maior valor sorteado foi {sorted(numAle)[-1]}')
print(f'O menor valor sorteado foi {sorted(numAle)[0]} \n')