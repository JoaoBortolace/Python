def notas(*nota, sit=False):
    """
    --> Função para analisar notas e a situação de um aluno(a)
    :param nota: Recebe as notas, pode receber uma ou mais (aceita várias)
    :param sit: (opcional) Adiciona ao dicionário a situação do aluno(a):
     Se média >= 7: situação = BOA
     Se 5 <= média < 7: situação = RAZOÁVEL
     Se média < 5: situação = RUIM
    :return: Retorna um dicionário contendo o total de notas, a maior, a menor, a média, e pode retornar a situação
    """
    notas_dic = {
        'total': len(nota),
        'maior': max(nota),
        'menor': min(nota),
        'média': sum(nota)/len(nota)
    }
    if sit:
        if notas_dic['média'] >= 7:
            notas_dic['situação'] = 'BOA'
        elif 5 <= notas_dic['média'] < 7:
            notas_dic['situação'] = 'RAZOÁVEL'
        else:
            notas_dic['situação'] = 'RUIM'
    return notas_dic


# Programa Principal
resp = notas(5, 10, 0, sit=True)
print(resp)
help(notas)
