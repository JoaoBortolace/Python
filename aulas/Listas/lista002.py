from random import randint

valores = list()  # Outra forma de fazer lista
valores.append(5)
valores.append(9)
valores.append(4)

for count in range(0, 5):
    valores.append(randint(0, 10))

# O acesso a dados da lista funciona que nem o da tupla
for valor in valores:
    print(f'{valor}...', end='')
print('')
for pos, valor in enumerate(valores):
    print(f'{valor} na posição {pos+1}')
