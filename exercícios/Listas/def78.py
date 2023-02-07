# Leia 5 valores do teclado, guarde em uma lista, e exiba o maior e o menor e suas posições
valores = list()
for count in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {count}: ')))
print(20*'-=-')
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for pos, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{pos}... ', end='')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for pos, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{pos}... ', end='')
