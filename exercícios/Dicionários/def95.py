jogadores = []
while True:
    print('-' * 30)

    carreira = {'nome': str(input('Nome do Jogador: ')), 'gols': []}
    numPartidas = int(input(f"Quantas partidas {carreira['nome']} jogou? "))
    for p in range(0, numPartidas):
        carreira['gols'].append(int(input(f'Quantos gols na partida {p}? ')))
    carreira['total'] = sum(carreira['gols'])

    jogadores.append(carreira.copy())
    carreira.clear()

    resp = str(input('Quer continuar? [S/N] ').strip())
    if resp in 'Nn':
        break

print(jogadores)

print('-=' * 30)
print(f"{'cod':<4}{'nome':<8}{'gols':>12}{'total':>15}")
print('-' * 40)
for j, c in enumerate(jogadores):
    print(f"{j:<4}{c['nome']:<16}{c['gols']}{'':<8}{c['total']:>6}")

while True:
    print('-' * 40)
    jogador = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if jogador == 999:
        print('<<< VOLTE SEMPRE >>>')
        break
    elif jogador < 0 or jogador > len(jogadores) - 1:
        print(f'ERRO! Não existe jogador com código {jogador}! Tente novamente')
    else:
        for j, g in enumerate(jogadores[jogador]['gols']):
            print(f'\t=> No jogo {j}, fez {g} gols.')
