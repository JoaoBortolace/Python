valores = []
while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    vai = ''
    while vai != 'N' and vai != 'S':
        vai = str(input('Quer continuar? [S/N] ')).strip().upper()
    if vai == 'N':
        break
print(30 * '-=')
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(valores, reverse=True)}')
if 5 in valores:
    print(f'O valor 5 faz parte da lista! {valores.count(5)} foram encontrados')
else:
    print('O valor 5 não foi encontrado na lista!')
