# Podemos passar estruturas complexas como parâmetros
# Tuplas, Listas
def dobra(lst):
    for v in range(0, len(lst)):
        lst[v] *= 2


valores = [2, 3, 6, 5, 8, 9, 10, 1]
dobra(valores)  # uma lista está sendo passada como parâmetro
print(valores)
