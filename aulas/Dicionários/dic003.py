pessoas = list()
pessoa = dict()

for c in range(0, 3):
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo: '))
    pessoa['Idade'] = str(input('Idade: '))
    # Para dicionários, o fatiamento não é possível
    # Para contornar essa limitação, exite o método copy
    # Ele passa os dados, e não cria uma relação
    # Assim, ao se alterar os dados em um, não altera noutro
    pessoas.append(pessoa.copy())

for p in pessoas:
    for k, v in p.items():
        print(f'{k}: {v}')
