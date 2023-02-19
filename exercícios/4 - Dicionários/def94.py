grupo = []
idadeSoma = media = 0
while True:
    pessoa = {'nome': str(input('Nome: ')).strip(), 'sexo': ''}
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('\033[31mERRO! Por favor, digite apenas M ou F.\033[m')
    pessoa['idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())
    idadeSoma += pessoa['idade']

    while True:
        vai = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if vai in 'SN':
            break
        print('\033[31mERRO! Por favor, digite apenas S ou N.\033[m')
    if vai == 'N':
        break

media = idadeSoma / len(grupo)
print('-=' * 30)
print(f'- O grupo tem {len(grupo)} pessoas.')
print(f'- A média de idade é de {media:5.2f} anos.')
print('- As mulheres cadastrads foram: ', end='')
for n, p in enumerate(grupo):
    if p['sexo'] == 'F':
        print(p['nome'], end='')
        if n < len(grupo) - 1:
            print(', ', end='')
print('\n- Lista das pessoas que estão acima da média: ')
for p in grupo:
    if p['idade'] > media:
        print()
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')
