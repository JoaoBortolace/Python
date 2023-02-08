# Para iniciar uma lista composta
# Basta colocar chaves em cada elementos
# Estas chaves são outras listas
# Este exemplo possui uma lista com 4 elementos
# Cada elementos é uma lista com 2 dados
galera = [['Mateus', 20], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)  # Assim acessa todos os dados da lista composta
print(galera[1])  # Já desta forma acessa todos os dados de uma das listas presente na lista composta
print(galera[1][0])  # E aqui acessa um dado de uma lista da lista composta

for p in galera:  # Cada elemento do for aqui será uma lista da lista composta
    print(f'{p[0]} tem {p[1]} anos de idade.')

