valor = list()
for i in range(0, 5):
    v = int(input('Digite um valor: '))
    if i == 0 or v > valor[-1]:
        valor.append(v)
        print('Adicionado ao final da lista...')
    else:
        for pos, vpos in enumerate(valor):
            if v <= vpos:
                valor.insert(pos, v)
                print(f'Adicionado na posição {pos} da lista...')
                break
print(30 * '-=')
print(f'Os valores digitados em ordem forma {valor}')
