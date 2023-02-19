# Escopo das variáveis
# O escopo é aonde as variáveis existem
# Podem ser: globais ou locais

def func():
    n2 = 2  # Variável local que só exite na função
    n1 = 4  # O python vai criar uma variável local
    # Mesmo já existindo uma variável global com o mesmo nome
    print(f'N1 dentro vale {n1}')  # Será dada a prioridade a variáveis locais
    print(f'N2 dentro vale {n2}')


def func2():
    global n1  # Usando este comando não será criado uma variável local, mas sim usará a global
    n1 = 5  # Altera o valor da global, não cria uma local
    print(f'N1 dentro vale {n1}')


n1 = 2  # Global
n2 = 3
func()
print(f'N1 fora vale {n1}')
# print(f'N2 fora vale {n2}') # Dará erro, pois ela não exite fora da função
func2()
print(f'N1 fora vale {n1}')
