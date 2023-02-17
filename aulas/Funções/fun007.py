# É possível retorna valores de funções
def somar(a=0, b=0, c=0):
    s = a+b+c
    return s  # Com esse comando a função retornará o valor da variável s


r1 = somar(3, 2, 5)  # O valor de r1 será o retorno da função somar
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}.')
