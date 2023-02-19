a = [2, 3, 4, 7]
b = a  # Quando se faz isso, é como se passasse um "ponteiro", a mesma lista é passada não uma cópia
b[2] = 8  # Ou seja, quando alterar algun item da lista B, a lista A será alterada também
c = a[:]  # Já isso, passa a cópia de todos os elementos de A, logo não possui ligação
c[2] = 6  # Portanto, isso só altera a lista C, a lista A fica inalterada
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')
