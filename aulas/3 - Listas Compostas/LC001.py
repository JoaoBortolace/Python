# 2 - 2 - Listas compostas são listas em listas
# Onde cada posição de uma lista "pai" tem uma lista "filho"
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)  # Assim colocamos a lista teste como dado da lista galera
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])  # Já assim passa os dados da lista teste para a lista galera, vai como lista
print(galera)
