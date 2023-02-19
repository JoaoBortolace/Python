valores = []
for count in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {count}: ')))
print('-=' * 30)
print(f'Você digitou os valores {valores}')
maior = max(valores)
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for pos, valor in enumerate(valores):
    if valor == maior:
        print(f'{pos}... ', end='')
menor = min(valores)
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for pos, valor in enumerate(valores):
    if valor == menor:
        print(f'{pos}... ', end='')
