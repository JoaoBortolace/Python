times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo',
         'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')

print(20*'-=-')
print(f'Lista de times do Brasileirão: {times}')
print(20*'-=-')
print(f'Os 5 primeiros são: {times[:5]}')
print(20*'-=-')
print(f'Os 4 últimos são: {times[-4:]}')
print(20*'-=-')
print(f'Times em ordem alfabética: {sorted(times)}')
print(20*'-=-')
print(f"O Santos está na {times.index('Santos')+1}ª posição")
