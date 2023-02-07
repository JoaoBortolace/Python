valor = list()
for i in range(0, 5):
    v = int(input('Digite um valor: '))
    if len(valor) == 0:
        valor.append(v)
        print('Adicionado ao final da lista...')
    else:
        if v >= max(valor):
            valor.append(v)
            print('Adicionado ao final da lista...')
        else:
            for j in range(0, len(valor)):
                if v < valor[j]:
                    valor.insert(j, v)
                    print(f'Adicionado na posição {j} da lista...')
                    break
print(30*'-=')
print(f'Os valores digitados em ordem forma {valor}')
