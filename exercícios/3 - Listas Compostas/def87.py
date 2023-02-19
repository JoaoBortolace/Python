matriz = [[], [], []]
somaPar = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))
        if matriz[i][j] % 2 == 0:
            somaPar += matriz[i][j]

print('-=' * 30)
for linha in matriz:
    for elemento in linha:
        print(f'[{elemento:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {somaPar}')
print(f'A soma dos valores da terceira coluna é {matriz[0][2]+matriz[1][2]+matriz[2][2]}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
