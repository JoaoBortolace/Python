# 4 - 4 - Dicionários, são estruturas de dados compostas com 1 - 1 - Tuplas e listas
# dicionários são parecidos com listas, porém podem usar literais "palavras" como indentificadores
# Em listas [ 0, 1, 2, 3, ...], em dicionários {dado1: , dado2: , dado3: ,...}
# Para instanciar um dicionário, exitem duas formas:
dic1 = dict()
dic2 = {
    'nome': 'Pedro',
    'idade': 25
}
lista = ['Pedro', 25]  # Estrutura similar da acima, porém como acessamos o dado é diferente
print(lista[0], lista[1])  # Em lista usamos o número da posição para acesar o dado
print(dic2['nome'], dic2['idade'])  # Já em dicionários, usamos o nome da posição para acessar

# Para adicionar dados é bem simples
# O append usado nas listas não funciona em dicionários
# Basta colocar o nome da posição querido e o dado dela
dic2['sexo'] = 'M'
print(dic2)

# Remove elementos, use o del e coloque o nome da posição
del dic2['idade']
print(dic2)
