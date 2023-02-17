# Funções são estruturas desenvolvidas para substituir rotinas
# Assim evitando ficar repetindo o código

# Como, por exemplo, ao invés de ficar repetindo o codigo
# Pode-se substituir por uma função que recebe dois parâmetros
# E realiza as ações desejadas
def soma(x, y):
    print(f'x = {x} e y = {y}')
    print(f'A soma X+Y = {x+y}')


# E quando precisamos da função chamamos elas, passando os parâmetros
a = 4
b = 5
s = a + b
print(s)
soma(4, 5)  # Este unico comando substitui as linhas acima

a = 8
b = 9
s = a + b
print(s)
soma(x=8, y=9)  # Podemos explicitar as variáveis dos parâmetros

a = 2
b = 1
s = a + b
print(s)
soma(y=2, x=1)  # E assim podemos inverter a ordem
