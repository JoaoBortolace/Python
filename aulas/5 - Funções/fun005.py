# As funções podem ter parâmetros opcionais, ou parâmetros com valores padrões
def somar(a, b, c=0):
    # Neste exemplo, o parâmetro 'C', é opcional
    """
    — > Faz a soma de três valores e mostra o resultado na tela
    :param a: Primeiro valor — Obrigatório
    :param b: Segundo valor — Obrigatório
    :param c: Terceiro valor — Opcional, caso não seja passado será igual a 0
    :return: Sem retorno
    """
    s = a+b+c
    print(f'A soma vale {s}')


help(somar)
somar(1, 3, 2)
somar(1, 2)  # Funcionará pois o terceiro parâmetro é opcional
somar(1)  # Erro, pois o segundo parâmetro não é opcional
