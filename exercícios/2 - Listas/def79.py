valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(valor)
    r = ''
    while r != 'N' and r != 'S':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r == 'N':
        break
valores.sort()
print(30 * '-=')
print(f'Você digitou os valores {valores}')
