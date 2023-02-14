from datetime import date
cadastro = {'nome': str(input('Nome: '))}
anoNascimento = int(input('Ano de Nascimento: '))
cadastro['idade'] = date.today().year - anoNascimento
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] > 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: R$').replace(',', '.'))
    cadastro['aposentadoria'] = (cadastro['contratação'] + 35) - anoNascimento
print('-=' * 30)
for k, v in cadastro.items():
    print(f'  - {k} tem o valor {v}')
