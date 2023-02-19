def ficha(nome='', gols=0):
    if nome == '':
        nome = '<desconhecido>'
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-' * 30)
name = str(input('Nome do Jogador: '))
gol = str(input('Número de Gols: '))
if gol == '' or not gol.isnumeric():
    gol = 0
ficha(name, gol)
