carreira = {'nome': str(input('Nome do Jogador: ')), 'gols': []}
numPartidas = int(input(f"Quantas partidas {carreira['nome']} jogou? "))
for p in range(0, numPartidas):
    carreira['gols'].append(int(input(f'\tQuantos gols na partida {p}? ')))
carreira['total'] = sum(carreira['gols'])
print('-=' * 30)
print(carreira)
print('-=' * 30)
for k, v in carreira.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f"O jogador {carreira['nome']} jogou {len(carreira['gols'])} partidas.")
for j, g in enumerate(carreira['gols']):
    print(f'\t=> Na partida {j}, fez {g} gols.')
print(f"Foi um total de {carreira['total']} gols.")
