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
print(f'A lista completa é {valores}')
par = list()
impar = list()
for num in valores:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
