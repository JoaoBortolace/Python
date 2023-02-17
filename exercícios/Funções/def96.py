def area(larg, comp):
    print(f'A área de um terreno {larg}x{comp} é de {larg * comp}m².')


# Programa Principal
print(' Controle de Terrenos')
print('-' * 22)
lar = float(input('LARGURA (m): ').replace(',', '.'))
com = float(input('COMPRIMENTO (m): ').replace(',', '.'))
area(lar, com)
