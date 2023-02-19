def aumentar(n, p=0, fot=True):
    if fot:
        return moeda(n*(1+abs(p)/100))
    return n*(1+abs(p)/100)


def diminuir(n, p=0, fot=True):
    if fot:
        return moeda(n*(1-abs(p)/100))
    return n*(1-abs(p)/100)


def metade(n, fot=True):
    if fot:
        return moeda(n/2)
    return n/2


def dobro(n, fot=True):
    if fot:
        return moeda(2*n)
    return 2*n


def moeda(p):
    return f'R${p:.2f}'.replace('.', ',')


def resumo(p, a=0, r=0):
    print('-' * 30)
    print(' '*7 + 'RESUMO DO VALOR')
    print('-' * 30)
    print(f'Preço analisado:     {moeda(p)}')
    print(f'Dobro do preço:      {dobro(p)}')
    print(f'Metade do preço:     {metade(p)}')
    if a != 0:
        print(f'{a}% de aumento:      {aumentar(p, a)}')
    if r != 0:
        print(f'{r}% de redução:      {diminuir(p, r)}')
