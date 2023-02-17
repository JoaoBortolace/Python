def area(la, c):
    print(f'A área de um terreno {la}x{c} é de {la*c}m².')


print(' Controle de Terrenos')
print('-' * 22)
lar = float(input('LARGURA (m): ').replace(',', '.'))
com = float(input('COMPRIMENTO (m): ').replace(',', '.'))
area(lar, com)
