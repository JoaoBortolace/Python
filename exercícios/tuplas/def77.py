palavras = (str, str, str, str, str, str)
p1 = str(input('Palavra 1: '))
p2 = str(input('Palavra 2: '))
p3 = str(input('Palavra 3: '))
p4 = str(input('Palavra 4: '))
p5 = str(input('Palavra 5: '))
p6 = str(input('Palavra 6: '))

palavras = (p1, p2, p3, p4, p5, p6)

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra in 'aieou':
            print(letra, end=' ')
