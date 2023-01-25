#Geometria Analítica
"""
1 - Distância entre dois pontos
2 - Ponto médio
3 - Condição de alinhamento de três pontos
4 - equação geral da reta
5 - equação reduzida da reta
"""

from math import sqrt, trunc, radians, tan
from time import sleep

print('Geometria Analítica')
def dist_2_p():
    print('A(x, y):')
    ax = float(input('x: '))
    ay = float(input('y: '))
    print('B(x, y):')
    bx = float(input('x: '))
    by = float(input('y: '))
    dist = sqrt((ax-bx)**2 + (ay-by)**2)
    print(f'A distância entre os pontos A({ax}, {ay}) e B({bx}, {by}): {dist}.')
 

def p_medio():
    print('A(x, y):')
    ax = float(input('x: '))
    ay = float(input('y: '))
    print('B(x, y):')
    bx = float(input('x: '))
    by = float(input('y: '))
    mx = trunc((ax + bx)/2)
    my = trunc((ay + by)/2)
    print(f'O ponto médio entre os pontos A({ax}, {ay}) e B({bx}, {by}): M({mx}, {my}).') 


def coal_3_p():
    print('A(x, y):')
    ax = float(input('x: '))
    ay = float(input('y: '))
    print('B(x, y):')
    bx = float(input('x: '))
    by = float(input('y: '))
    print('C(x, y):')
    cx = float(input('x: '))
    cy = float(input('y: '))
    dp = (ax*by) + (ay*cx) + (bx*cy)
    ds = (ay*bx) + (ax*cy) + (by*cx)
    d = dp - ds
    if d != 0:
        print('Os pontos não estão alinhados.')
        print(f'A área do triângulo formados por ele {d/2}.')
    else:
        print(f'Os pontos A({ax}, {ay}), B({bx}, {by}) e C({cx}, {cy}) estão alinhados.')


def equal_g():
    print('A(x, y):')
    ax = float(input('x: '))
    ay = float(input('y: '))
    print('B(x, y):')
    bx = float(input('x: '))
    by = float(input('y: '))
    a = ay - by
    b = bx - ax
    c = (ax*by) - (ay*bx)
    if b > 0:
        b = '+' + str(b)
    if c > 0:
        c = '+' + str(c)
    print(f'A equação geral da reta é {a}x {b}y {c} = 0')


def equal_r():
    print('Ângulo ou coeficiente ângular:')
    print(' 1- Ângulo \n 2- Coeficiente ângular')
    res = int(input('Qual? ').strip().replace(',', ''))
    if res == 1:
        print('A(x, y):')
        ax = float(input('x: '))
        ay = float(input('y: '))
        alpha = radians(float(input('α = ')))
        m = trunc(tan(alpha))
        n = trunc(ay-(m*ax))
        if m > 0:
            m = '+ ' + str(m)
        elif m == -1:
            m = '-'
        if n > 0:
            n = '+ ' + str(n)
        print(f'A equação reduzida da reta é y = {m}x {n}')
    elif res == 2:
        print('A(x, y):')
        ax = float(input('x: '))
        ay = float(input('y: '))
        print('B(x, y):')
        bx = float(input('x: '))
        by = float(input('y: '))
        m = (ay - by)/(ax - bx)
        if ax == 0 or m == 0:
            print(f'A equação reduzida da reta é y = {m}x')  
        else:
            n = ay-(m*ax)
            print(f'A equação reduzida da reta é y = {m}x + {n}')
    else:
        print('\033[1;31mOperação inválida! Insira novamente\033[m')
        equal_r()


def _repetir_():
        print('Deseja realiza outro calcúlo?')
        rr = input('[s]im ou [n]ão ')
        if rr == 'n':
            print('Até mais!')
            exit()
        elif rr =='s':
            return per() 
        else:
            print('\033[1;31mOperação inválida! Insira novamente\033[m')
            _repetir_()


def per():
    print('\nQual equação deseja realizar:')
    print(' 1- Distância entre dois pontos \n 2- Ponto médio \n 3- Alinhamento \n 4- Equação geral \n 5- Equação reduzida \n 6- Sair')
    res = int(input('Qual? ').strip().replace(',', ''))
    if res == 1:
        dist_2_p()
    elif res == 2:
        p_medio()
    elif res == 3:
        coal_3_p()
    elif res == 4:
        equal_g()
    elif res == 5:
        equal_r()
    elif res == 6:
        print('Até mais!')
        sleep(0.5)
        exit()
    else:
        print('\033[1;31mOperação inválida! Insira novamente\033[m')
        per()
    _repetir_()


per()