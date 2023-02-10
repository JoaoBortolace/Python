aluno = {'Nome': str(input('Nome: '))}
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: ').replace(',', '.'))
for k, v in aluno.items():
    print(f'{k} é igual {v}')
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
print(f'Situação é igual a {aluno["Situação"]}')
