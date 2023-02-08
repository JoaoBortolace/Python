preco = ('i9 13900K', 51571.90, 'RTX 4090', 12599.99, 'R9 7950X',
         4699.99, 'ARC A770', 2799.99, 'RX 7900XT', 7798.99)

print(45*'-')
print(f'{"LISTAGEM DE PREÇOS":^45}')
print(45*'-')

for i in range(0, len(preco), 2):
    print(f'{preco[i]:.<34}', end='')
    print(f'R${preco[i+1]:>9.2f}')
print(45*'-')
