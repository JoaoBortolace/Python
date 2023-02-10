from datetime import date
cadastro = {'nome': str(input('Nome: '))}
anoNascimento = int(input('Ano de Nascimento: '))
cadastro['idade'] = date.today().year - anoNascimento
ct = int(input('Carteira de Trabalho (0 não tem): '))
if ct > 0:
    cadastro['ctps'] = ct
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: R$').replace(',', '.'))
print('-=' * 30)
cadastro['aposentadoria'] = cadastro['contratação'] + 35 - anoNascimento
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')
