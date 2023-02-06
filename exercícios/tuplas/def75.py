n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

num = (n1, n2, n3, n4)
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
try:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição')
except(ValueError):
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram')
for n in num:
    if (n%2 == 0):
        print(n)