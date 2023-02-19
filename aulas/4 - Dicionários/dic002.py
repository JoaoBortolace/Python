# O nome das posições são chamados Chaves (Keys)
# E o dados das posições são chamados Valores (Values)
filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filme)
# Para acessar somente chaves (nomes das posições)
print(filme.keys())
# Para acessar somente os valores (dados das posições)
print(filme.values())
# Para acessar os dois
print(filme.items())
# Podemos usar esse metodos para fazer laços
for k, v in filme.items():
    print(f'O {k} é {v}')

filme2 = {
    'titulo': 'Avengers',
    'ano': 2012,
    'diretor': 'Joss Whedon'
}

filme3 = {
    'titulo': 'Matrix',
    'ano': 1999,
    'diretor': 'Wachowski'
}

# Podemos mistura as estruturas de dados, 1 - 1 - Tuplas, listas, dicionários
locadora = [filme, filme2, filme3]  # Aqui uma lista onde cada posição é um dicionário
print(locadora)
print(locadora[0]['ano'])  # Para acessar os elementos
print(locadora[2]['titulo'])
