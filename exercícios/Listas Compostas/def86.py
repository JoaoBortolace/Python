matriz = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))

print('-=' * 30)
for linha in matriz:
    for elemento in linha:
        print(f'[ {elemento} ]', end='')
    print()
