# Muitas vezes é necessário documentação sobre a função
# Para isso o python possiu a ajuda iterativa
# A função help() retorna a docstrings da função
# Outra forma é usar a "função".__doc__
def contador(inicio, fim, passo):
    # Para adicionar uma docstrings a uma função própria, basta abrir apas duplas três vezes
    """
    — > Faz uma contagem e mostra na tela
    :param inicio: Primeiro termo da contagem
    :param fim: Limite da contagem, não necessariamente o último termo, poís dependerá do passo
    :param passo: Valor de incremento/decremento da contagem, se passo for igual a zero, passo → 1. O sinal é
    corrigido conforme a nescessidade, passo == positivo com ínicio > fim, passo -> negativo, passo == negativo com
    ínicio <= fim, passo -> positivo
    :return: sem retorno
    """
    if passo == 0:
        passo = 1
    if (inicio > fim and passo > 0) or (inicio <= fim and passo < 0):
        passo *= -1
    fim_c = fim + 1 if inicio <= fim else fim - 1
    for i in range(inicio, fim_c, passo):
        print(i, end=' ', flush=True)
    print('FIM!')


help(contador)
