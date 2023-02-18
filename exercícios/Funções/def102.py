def fatorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o cálculo
    :return: O valor do Fatorial de n, n!
    """
    print('-' * 30)
    f = 1
    for i in range(num, 0, -1):
        if show and i > 0:
            print(i, end=' ')
            if i > 1:
                print('x ', end='')
        f *= i
    if show:
        return f'= {f}'
    return f


# Programa Principal
print(fatorial(8, True))
