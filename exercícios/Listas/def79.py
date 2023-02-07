valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(valor)
    vai = ''
    while vai != 'N' and vai != 'S':
        vai = str(input('Quer continuar? [S/N] ')).strip().upper()
    if vai == 'N':
        break
valores.sort()
print(15*'-=-')
print(f'Você digitou os valores {valores}')
