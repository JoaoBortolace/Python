from math import pow

print('Regressão Linear Simples, y(x) = α + βx')

n = int(input(' --- Conjuntos de dados --- \n n: '))
y = list(range(n))
x = list(range(n))
for i in range(0, n):
    x[i] = float(input('x = ').replace(',', '.'))
    y[i] = float(input(f'y({x[i]}) = ').replace(',', '.'))

ymed = 0
xmed = 0
xy = 0
sqrx = 0
for i in range(0, n):
    ymed += y[i]
    xmed += x[i]
    xy += x[i]*y[i]
    sqrx += pow(x[i], 2)

ymed = ymed/n
xmed = xmed/n
beta = (xy - (n*xmed*ymed))/(sqrx - n*pow(xmed, 2))
alpha = ymed - beta*xmed

sqt = 0
sqres = 0

for i in range(0, n):
    sqt += pow((y[i] - ymed), 2)
    sqres += pow( (y[i] - (alpha + beta*x[i])), 2)
sqr = sqt - sqres
r = sqr/sqt
F = sqr/(sqres/(n-2))


print(f'y(x) = {alpha:.3f} + {beta:.3f}x, R² = {r:.3f}')
input('Aperte qualquer tecla para sair.')