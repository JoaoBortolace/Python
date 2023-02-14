aluno = {'Nome': str(input('Nome: '))}
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: ').replace(',', '.'))

if aluno['Média'] >= 7:
    aluno['Situação'] = '\033[36mAprovado\033[m'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = '\033[33mRecuperação\033[m'
else:
    aluno['Situação'] = '\033[31mReprovado\033[m'
print('-=' * 30)
for k, v in aluno.items():
    print(f'\t- {k} é igual a {v}.')
