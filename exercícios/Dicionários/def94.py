grupo = []
idadeSoma = 0
while True:
    pessoa = {'nome': str(input('Nome: ').strip()), 'sexo': ''}
    while pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F':
        pessoa['sexo'] = str(input('Sexo: [M/F] ').strip().upper())
    pessoa['idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())
    idadeSoma += pessoa['idade']

    vai = str(input('Quer continuar? [S/N] ').strip())
    if vai in 'Nn':
        break

print('-=' * 30)
print(f'- O grupo tem {len(grupo)} pessoas.')
print(f'- A média de idade é de {idadeSoma/len(grupo)} anos.')
print('- As mulheres cadastrads foram: ', end='')
for n, p in enumerate(grupo):
    if p['sexo'] == 'F':
        print(p['nome'], end='')
        if n < len(grupo) - 1:
            print(', ', end='')
print('\n- Lista das pessoas que estão acima da média: ')
for p in grupo:
    if p['idade'] > idadeSoma/len(grupo):
        print()
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')
