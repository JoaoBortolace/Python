pessoasCadrastradas = []
maior = 0
menor = 0
while True:
    pessoa = [str(input('Nome: ')).strip(), int(input('Peso(kg): '))]
    if len(pessoasCadrastradas) == 0:
        maior = menor = pessoa[1]
    elif pessoa[1] > maior:
        maior = pessoa[1]
    elif pessoa[1] < menor:
        menor = pessoa[1]
    pessoasCadrastradas.append(pessoa[:])
    resp = ''
    while resp != 'S' and resp != 'N':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoasCadrastradas)} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in pessoasCadrastradas:
    if p[1] == maior:
        print(p[0], end=' ')
print(f'\nO menor peso foi de {menor}kg. Peso de ', end='')
for p in pessoasCadrastradas:
    if p[1] == menor:
        print(p[0], end=' ')
