exp = str(input('Digite a expressão: '))
pilha = []
num = False
teste = False
for ele in exp:
    if ele == '(':
        pilha.append('(')
    elif ele == ')':
        if num == 0:
            teste = True
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
    else:
        if len(pilha) > 0:
            num = True
        else:
            num = False
if len(pilha) == 0 and not teste:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
